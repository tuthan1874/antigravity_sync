# CRM Outreach Module — Phase 1 Walkthrough

## Summary
Successfully rebuilt the Email Outreach module from campaign-centric to **lead-centric** architecture, following the KI handoff guide.

## Changes Made

### Database (Supabase)
- **Dropped** 4 old tables: `crm_email_campaigns`, `crm_email_templates`, `crm_email_leads`, `crm_email_logs`
- **Created** 3 new tables:
  - `crm_outreach_leads` — 1 row per contact, tracks full 3-step sequence lifecycle
  - `crm_email_log` — 1 row per email sent, references lead
  - `crm_email_templates` — 3 sequence steps with A/B subject lines
- **Seeded** 3 email templates with real HTML content from source files
- All tables have RLS enabled + proper indexes

### TypeScript Types ([types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts#L323-L362))
- Replaced `CrmEmailCampaign`, `CrmEmailLead`, old `CrmEmailLog`, old `CrmEmailTemplate`
- New: `CrmOutreachLead`, `CrmEmailLog`, `CrmEmailTemplate` matching DB schema

### Service Layer ([outreachService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/services/outreachService.ts))
- Lead CRUD (create, batch create, update, delete, fetch with filters)
- Template CRUD (fetch, update)
- Email log fetching
- Pipeline stats aggregation
- CSV parser supporting SalesQL format
- FastAPI integration stubs (Discovery + Send)

### UI Component ([EmailOutreach.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/EmailOutreach.tsx))
4 sub-tabs:

| Tab | Features |
|-----|----------|
| **Dashboard** | Stats cards (Total, Tier 1/2/3), Pipeline funnel visualization, Key metrics (Send/Reply/Bounce rate) |
| **Leads** | Searchable/filterable table, CSV import (SalesQL format), CRM import, Manual add, Status management, Delete |
| **Discovery** | Company + Domain input → FastAPI integration (Phase 2) |
| **Templates** | 3-step sequence timeline, Subject line A/B variants, HTML editor with variable buttons, Fullscreen email preview |

## Testing & Validation

- ✅ `vite build` — Success
- ✅ Dashboard renders pipeline funnel with real-time stats
- ✅ Leads tab — Add lead, filter by status/tier, search
- ✅ Templates tab — 3 steps displayed with subject lines, Preview modal works
- ✅ Discovery tab — UI renders, correctly shows API not configured error

## Screenshots

````carousel
![Dashboard Tab — Pipeline funnel with 2 test leads](file:///C:/Users/dangt/.gemini/antigravity/brain/f7544c32-6f19-4a7d-80b9-bfa461c717ee/.system_generated/click_feedback/click_feedback_1776616192644.png)
<!-- slide -->
![Templates Tab — 3-step email sequence with subject variants](file:///C:/Users/dangt/.gemini/antigravity/brain/f7544c32-6f19-4a7d-80b9-bfa461c717ee/.system_generated/click_feedback/click_feedback_1776616135256.png)
<!-- slide -->
![Leads Tab — 2 test leads with tier badges and status dropdowns](file:///C:/Users/dangt/.gemini/antigravity/brain/f7544c32-6f19-4a7d-80b9-bfa461c717ee/.system_generated/click_feedback/click_feedback_1776615417517.png)
<!-- slide -->
![Discovery Tab — Company + Domain input for FastAPI integration](file:///C:/Users/dangt/.gemini/antigravity/brain/f7544c32-6f19-4a7d-80b9-bfa461c717ee/.system_generated/click_feedback/click_feedback_1776615439039.png)
````

## Next Steps (Phase 2)
- Deploy FastAPI on **Megahost_02** (180.93.144.98) at `/opt/td-mailer-api/` port 8401
- Migrate `email_discovery_bot.py` → `/api/leads/discover` endpoint
- Migrate `cold_email_sender.py` → `/api/email/send` endpoint
- Set `VITE_OUTREACH_API_URL` in frontend `.env`
