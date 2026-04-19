# Email Outreach → CRM Handoff Guide

## Quick Reference

### File Locations (Current Workspace)

```
e:\TDC_App\TDGAMES_App\Client_Data\
├── cold_email_sender.py              # Core email sending logic (reuse for FastAPI)
├── setup_gmail_oauth.py              # OAuth setup script
├── credentials/
│   └── gmail_token.json              # Gmail API token (SENSITIVE)
├── email_templates/
│   ├── initial_outreach.html         # Email 1: First contact
│   ├── followup_1.html              # Email 2: Portfolio highlight (Day 3)
│   ├── followup_2.html              # Email 3: Breakup + free trial (Day 7)
│   └── sequence_config.json         # Subject lines + sequence config
├── output/
│   └── SalesQL_Enriched_Leads.csv   # 553 contacts (131 unique studios)
├── B2B_Lead_Pipeline/
│   ├── README.md                    # Full integration guide
│   ├── email_discovery_bot.py       # Lead discovery pipeline (26KB)
│   ├── data_cleaning_script.py      # Studio list cleaner
│   ├── export_excel.py              # Excel report generator
│   ├── Cleaned_Target_Studios.csv   # 278 studios input
│   └── .env                        # API keys
└── .env                             # API keys (SalesQL, Google CSE)
```

### Billing App Location
```
e:\TDC_App\TDGAMES_App\td-games-invoice-app\   # Local clone of tdgames_billing
```

---

## Full CRM Outreach Flow

```
┌──────────────────────────────────────────────────────────────┐
│                    CRM Outreach Module                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  [1] LEAD DISCOVERY (from company name)                      │
│      Input: Company Name + Domain                            │
│      ├── Web Scraping → contact@, info@ emails              │
│      ├── Google CSE → LinkedIn profiles (Tier 1 priority)   │
│      └── SalesQL API → Enrich → Work Email + Personal Email │
│      Output: Enriched contacts with Tier ranking             │
│                                                              │
│  [2] LEAD MANAGEMENT                                         │
│      ├── Import from CSV / manual add / discovery results    │
│      ├── Table view with filter (Tier/Status)               │
│      ├── Dedup per studio (best contact only)               │
│      └── Convert Lead → CRM Client                          │
│                                                              │
│  [3] EMAIL OUTREACH                                          │
│      ├── Template preview with personalization               │
│      ├── Send single / batch (with rate limiting)           │
│      ├── 3-email sequence: initial → followup1 → followup2  │
│      └── Auto follow-up (cron: 3 days / 7 days)            │
│                                                              │
│  [4] TRACKING & ANALYTICS                                    │
│      ├── Sent log (timestamp, status, message ID)           │
│      ├── Reply detection (Gmail inbox scan)                 │
│      ├── Bounce detection                                    │
│      └── Pipeline funnel: Pending→Sent→Follow-up→Replied    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Architecture: Hybrid (SPA + VPS API)

```
app.tdgamestudio.com (React SPA)
  │
  ├── /api/email/*    → FastAPI localhost:8401  (email sending)
  ├── /api/leads/*    → FastAPI localhost:8401  (lead discovery)
  └── Supabase        → Direct client SDK      (CRUD data)

VPS FastAPI (/opt/td-mailer-api/) handles:
  ├── Gmail API sending (OAuth token)
  ├── Lead discovery (web scraping, Google CSE, SalesQL)
  └── Inbox scanning (reply/bounce detection)

Supabase stores:
  ├── crm_outreach_leads  (lead data)
  ├── crm_email_log       (sent history)
  └── crm_email_templates (HTML templates)
```

---

## TypeScript Types to Add

```typescript
// ── CRM Outreach ─────────────────────────────────────────
export interface CrmOutreachLead {
    id: string;
    client_id: string | null;
    studio_name: string;
    contact_name: string;
    first_name: string;
    email: string;
    job_title: string;
    linkedin_url: string;
    tier: number;
    outreach_status: 'pending' | 'initial_sent' | 'followup1_sent' | 'followup2_sent' | 'replied' | 'bounced' | 'unsubscribed';
    initial_sent_at: string | null;
    followup1_sent_at: string | null;
    followup2_sent_at: string | null;
    replied_at: string | null;
    source: string;
    tags: string[];
    notes: string;
    created_at: string;
    updated_at: string;
}

export interface CrmEmailLog {
    id: string;
    lead_id: string;
    template_name: string;
    to_email: string;
    subject: string;
    gmail_message_id: string;
    status: 'sent' | 'bounced' | 'failed';
    error_message: string;
    sent_at: string;
}

export interface CrmEmailTemplate {
    id: string;
    name: string;
    subject_template: string;
    html_content: string;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}
```

---

## Supabase Migration SQL

```sql
-- crm_outreach_leads
CREATE TABLE crm_outreach_leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID REFERENCES crm_clients(id) ON DELETE SET NULL,
    studio_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    first_name TEXT DEFAULT '',
    email TEXT NOT NULL,
    job_title TEXT DEFAULT '',
    linkedin_url TEXT DEFAULT '',
    tier INTEGER DEFAULT 3,
    outreach_status TEXT DEFAULT 'pending',
    initial_sent_at TIMESTAMPTZ,
    followup1_sent_at TIMESTAMPTZ,
    followup2_sent_at TIMESTAMPTZ,
    replied_at TIMESTAMPTZ,
    source TEXT DEFAULT 'salesql',
    tags TEXT[] DEFAULT '{}',
    notes TEXT DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- crm_email_log
CREATE TABLE crm_email_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES crm_outreach_leads(id) ON DELETE CASCADE,
    template_name TEXT NOT NULL,
    to_email TEXT NOT NULL,
    subject TEXT NOT NULL,
    gmail_message_id TEXT,
    status TEXT DEFAULT 'sent',
    error_message TEXT,
    sent_at TIMESTAMPTZ DEFAULT NOW()
);

-- crm_email_templates
CREATE TABLE crm_email_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT UNIQUE NOT NULL,
    subject_template TEXT NOT NULL,
    html_content TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- RLS
ALTER TABLE crm_outreach_leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm_email_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm_email_templates ENABLE ROW LEVEL SECURITY;
CREATE POLICY "auth_manage_outreach" ON crm_outreach_leads FOR ALL USING (auth.role() = 'authenticated');
CREATE POLICY "auth_manage_email_log" ON crm_email_log FOR ALL USING (auth.role() = 'authenticated');
CREATE POLICY "auth_manage_templates" ON crm_email_templates FOR ALL USING (auth.role() = 'authenticated');

-- Indexes
CREATE INDEX idx_outreach_status ON crm_outreach_leads(outreach_status);
CREATE INDEX idx_outreach_tier ON crm_outreach_leads(tier);
CREATE INDEX idx_email_log_lead ON crm_email_log(lead_id);
```

---

## FastAPI Endpoints (VPS)

### Email Sending
| Method | Endpoint | Mô tả |
|--------|----------|--------|
| POST | `/api/email/send` | Gửi email cho 1 lead |
| POST | `/api/email/batch` | Gửi batch (rate limiting) |
| POST | `/api/email/test` | Gửi test email |
| GET | `/api/email/status` | Today's quota |
| POST | `/api/email/preview` | Render template preview |
| POST | `/api/inbox/scan` | Check replies/bounces |

### Lead Discovery
| Method | Endpoint | Mô tả |
|--------|----------|--------|
| POST | `/api/leads/discover` | Input: company+domain → enriched contacts |
| POST | `/api/leads/enrich` | Enrich single LinkedIn URL |
| POST | `/api/leads/batch` | Batch discover (with progress) |
| GET | `/api/leads/export` | Download Excel report |

---

## Key Python Functions to Reuse

From `email_discovery_bot.py`:
- `scrape_general_emails(domain)` → public emails
- `find_and_verify_domain_emails(domain)` → SMTP-verified
- `search_linkedin_targets(studio_name)` → LinkedIn URLs
- `salesql_enrich(linkedin_url)` → full contact info
- `get_title_tier(job_title)` → tier classification

From `cold_email_sender.py`:
- `get_gmail_service()` → Gmail API client
- `personalize(template, contact)` → template rendering
- `send_email(service, to, subject, html)` → send via Gmail
- `create_email(to, subject, html)` → MIME message

---

## Config & Credentials

| Key | Value |
|-----|-------|
| Sender Email | `toan.dang@tdgamestudio.com` |
| Sender Name | `Tony Dang` |
| Google Cloud Project | `email-mkt-493813` |
| OAuth Client ID | `71850303483-9jhtla0ngbdkr9p87esfreohq6incs9b` |
| Token Path | VPS: `/opt/td-mailer-api/credentials/gmail_token.json` |
| Rate Limit | 30 emails/day, 2-5min delay |
| SalesQL API Key | In `.env` |
| Google CSE Key | In `.env` |
| Google CX ID | In `.env` |

## Logo URLs (R2 CDN)
| Logo | URL |
|------|-----|
| White (dark bg) | `https://pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev/logo/logo_td_white.png` |
| Black (light bg) | `https://pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev/logo/logo_td_black.png` |
| No text (icon) | `https://pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev/logo/logo_td_notext.png` |

## Lead Data
- **553 contacts** / **131 unique studios**
- Tier 1 (Art Director): 110, Tier 2 (Producer): 7, Tier 3 (CEO): 5
- CSV: `e:\TDC_App\TDGAMES_App\Client_Data\output\SalesQL_Enriched_Leads.csv`

## VPS Deploy
- Server: Megahost_02 (180.93.144.98)  
- Path: `/opt/td-mailer-api/`
- Port: 8401
- Nginx: `app.tdgamestudio.com/api/email/` + `/api/leads/`
