# CRM Outreach Module — Revised Implementation Plan

Tái cấu trúc module Outreach theo KI handoff guide: **Lead-centric** thay vì campaign-centric, tích hợp 2 luồng: **Lead Discovery** + **Email Sending** qua FastAPI trên VPS.

## User Review Required

> [!IMPORTANT]
> **Breaking change:** Sẽ **drop 4 tables cũ** (`crm_email_campaigns/templates/leads/logs`) vừa tạo và thay bằng 3 tables mới theo KI schema. Campaign "Test Campaign Q2" sẽ bị xoá. OK?

> [!WARNING]
> **FastAPI sẽ deploy trên VPS nào?** KI ghi Megahost_02 (180.93.144.98) — nhưng check thấy VPS MCP đang connect tới VietNix. Cần confirm server target.

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│  CRM Outreach Tab (React SPA)                       │
│  ├── 📊 Dashboard  — stats + funnel pipeline        │
│  ├── 👥 Leads      — table, import CSV/CRM, manage  │
│  ├── 🔍 Discovery  — input company → find contacts  │
│  └── 📧 Emails     — templates, send, logs          │
└───────┬─────────────────────────────┬───────────────┘
        │ Supabase SDK (direct)       │ HTTP API
        ▼                             ▼
  ┌─────────────┐           ┌──────────────────────┐
  │  Supabase   │           │  FastAPI (VPS:8401)  │
  │  Tables:    │           │  ├── /api/email/send │
  │  • leads    │           │  ├── /api/email/test │
  │  • email_log│           │  ├── /api/leads/     │
  │  • templates│           │  │   discover        │
  └─────────────┘           │  └── Gmail API +     │
                            │      SalesQL + CSE   │
                            └──────────────────────┘
```

---

## Phase 1: DB Schema + Frontend (Bắt đầu ngay)

### Database Migration

#### [DROP] Old Phase 1 tables
```sql
DROP TABLE IF EXISTS crm_email_logs CASCADE;
DROP TABLE IF EXISTS crm_email_leads CASCADE;
DROP TABLE IF EXISTS crm_email_templates CASCADE;
DROP TABLE IF EXISTS crm_email_campaigns CASCADE;
```

#### [NEW] `crm_outreach_leads` — Lead-centric (1 row per contact)
| Column | Type | Description |
|--------|------|-------------|
| id | uuid PK | |
| client_id | uuid FK → crm_clients | Link CRM client |
| studio_name | text | Tên studio |
| contact_name | text | Tên liên hệ |
| first_name | text | First name (for personalization) |
| email | text | Best email |
| job_title | text | |
| linkedin_url | text | |
| tier | int | 1 (Art Director) / 2 (Producer) / 3 (CEO) |
| outreach_status | text | pending → initial_sent → followup1_sent → followup2_sent → replied / bounced |
| initial_sent_at | timestamptz | |
| followup1_sent_at | timestamptz | |
| followup2_sent_at | timestamptz | |
| replied_at | timestamptz | |
| source | text | 'csv_import' / 'crm_import' / 'discovery' / 'manual' |
| tags | text[] | |
| notes | text | |
| created_at, updated_at | timestamptz | |

#### [NEW] `crm_email_log` — Log mỗi email gửi đi
| Column | Type | Description |
|--------|------|-------------|
| id | uuid PK | |
| lead_id | uuid FK → leads | |
| template_name | text | 'initial_outreach' / 'followup_1' / 'followup_2' |
| to_email | text | |
| subject | text | |
| gmail_message_id | text | ID từ Gmail API |
| status | text | sent / bounced / failed |
| error_message | text | |
| sent_at | timestamptz | |

#### [NEW] `crm_email_templates` — 3 templates chính
| Column | Type | Description |
|--------|------|-------------|
| id | uuid PK | |
| name | text UNIQUE | 'initial_outreach' / 'followup_1' / 'followup_2' |
| subject_lines | text[] | A/B subject variants |
| html_content | text | Full HTML |
| delay_days | int | 0 / 3 / 7 |
| is_active | boolean | |
| created_at, updated_at | timestamptz | |

**Seed data:** Import 3 HTML templates + sequence_config.json subjects vào DB.

---

### Frontend Changes

#### [REPLACE] `apps/crm/components/EmailOutreach.tsx`
Complete rewrite with 3 sub-tabs:

**📊 Dashboard Sub-tab:**
- Pipeline funnel: Pending → Initial Sent → Follow-up 1 → Follow-up 2 → Replied
- Stats cards: Total leads, by tier, by status
- Today's send quota (from FastAPI)

**👥 Leads Sub-tab:**
- Table view: name, email, studio, tier, outreach_status, timestamps
- Filters: tier (1/2/3), status, source
- Import: CSV upload + CRM clients (reuse existing logic)
- Actions: Edit lead, delete, change status, convert to CRM client
- Bulk actions: select multiple → send initial email (Phase 2)

**🔍 Discovery Sub-tab:**
- Input form: Company Name + Domain
- "Discover Contacts" button → calls FastAPI → returns enriched contacts
- Results: table with contact_name, email, job_title, tier, linkedin
- "Add to Leads" button per result
- Batch discovery: upload CSV of domains

**📧 Email Sub-tab:**
- Template viewer: 3-step sequence timeline
- Template editor: Edit subject lines + HTML body
- HTML preview modal
- Send logs table (from crm_email_log)

#### [REPLACE] `apps/crm/services/outreachService.ts`
- CRUD for `crm_outreach_leads` (replace campaign-based logic)
- CRUD for `crm_email_log`
- CRUD for `crm_email_templates`
- CSV parser (keep existing)
- Stats calculator (pipeline counts)
- `discoverContacts(company, domain)` → calls FastAPI
- `sendEmail(leadId, templateName)` → calls FastAPI

#### [MODIFY] `types.ts`
- Replace 4 campaign interfaces with 3 new ones: `CrmOutreachLead`, `CrmEmailLog`, `CrmEmailTemplate` (from KI)

#### [NO CHANGE] `CrmApp.tsx`, `useCrmState.ts`
- Tab "📧 Outreach" already wired — chỉ cần component thay đổi nội bộ.

---

## Phase 2: FastAPI on VPS (Sau Phase 1)

Deploy FastAPI service on Megahost_02 at `/opt/td-mailer-api/`:

### Email Endpoints
| Method | Endpoint | Source |
|--------|----------|--------|
| POST | `/api/email/send` | Reuse `cold_email_sender.py` → `send_email()` |
| POST | `/api/email/test` | Reuse `cmd_test()` |
| GET | `/api/email/status` | Today's quota + sent count |
| POST | `/api/email/preview` | `personalize()` → return rendered HTML |

### Discovery Endpoints
| Method | Endpoint | Source |
|--------|----------|--------|
| POST | `/api/leads/discover` | Reuse `email_discovery_bot.py` functions |
| POST | `/api/leads/enrich` | `salesql_enrich(linkedin_url)` |

### Credentials
- Gmail token: Upload `credentials/gmail_token.json` to VPS
- API keys: `.env` with SalesQL, Google CSE keys
- Auth: API key header for security

---

## Execution Order

| # | Task | Files |
|---|------|-------|
| 1 | Drop old tables + create new schema | Supabase migration |
| 2 | Seed 3 email templates into DB | SQL INSERT |
| 3 | Update TypeScript types | types.ts |
| 4 | Rewrite outreachService.ts | outreachService.ts |
| 5 | Rewrite EmailOutreach.tsx | EmailOutreach.tsx |
| 6 | Build test | Vite build |
| 7 | UI verification | Browser test |

## Verification Plan

### Build
- `npx vite build` — no errors

### UI Testing
- Navigate to CRM → Outreach tab
- Verify 4 sub-tabs render correctly
- Import leads from CSV
- View template sequence with HTML preview
- Check pipeline dashboard stats
