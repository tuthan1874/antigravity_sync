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
└── .env                             # API keys (SalesQL, Google CSE)
```

### Billing App Location
```
e:\TDC_App\TDGAMES_App\td-games-invoice-app\   # Local clone of tdgames_billing
```

---

## What to Copy to Billing Project

### 1. Email Templates → Keep in Client_Data (FastAPI reads from here)
No need to copy. The FastAPI service on VPS will have its own copy.

### 2. TypeScript Types → Add to `types.ts`

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

### 3. Supabase Migration SQL

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

-- RLS Policies
ALTER TABLE crm_outreach_leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm_email_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm_email_templates ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Authenticated users can manage outreach leads"
    ON crm_outreach_leads FOR ALL USING (auth.role() = 'authenticated');
CREATE POLICY "Authenticated users can manage email log"
    ON crm_email_log FOR ALL USING (auth.role() = 'authenticated');
CREATE POLICY "Authenticated users can manage email templates"
    ON crm_email_templates FOR ALL USING (auth.role() = 'authenticated');

-- Indexes
CREATE INDEX idx_outreach_status ON crm_outreach_leads(outreach_status);
CREATE INDEX idx_outreach_tier ON crm_outreach_leads(tier);
CREATE INDEX idx_email_log_lead ON crm_email_log(lead_id);
CREATE INDEX idx_email_log_sent ON crm_email_log(sent_at);
```

### 4. New CRM Components to Create

```
apps/crm/components/
├── CrmApp.tsx                 # MODIFY: add "Outreach" tab
├── OutreachDashboard.tsx      # NEW: stats cards + pipeline funnel
├── LeadPipeline.tsx           # NEW: leads table with filters
├── EmailComposer.tsx          # NEW: preview + send email
├── CampaignLog.tsx            # NEW: sent email history
└── LeadImporter.tsx           # NEW: CSV import dialog

apps/crm/services/
└── crmService.ts              # MODIFY: add outreach CRUD functions

apps/crm/hooks/
└── useCrmState.ts             # MODIFY: add outreach state
```

### 5. Service Functions to Add (crmService.ts)

```typescript
// ── Outreach Leads ────────────────────────────────────────
export async function fetchOutreachLeads(filters?: {
    status?: string; tier?: number;
}): Promise<CrmOutreachLead[]> { ... }

export async function createOutreachLead(lead: Omit<CrmOutreachLead, 'id' | 'created_at' | 'updated_at'>): Promise<CrmOutreachLead> { ... }

export async function updateOutreachLead(id: string, updates: Partial<CrmOutreachLead>): Promise<void> { ... }

export async function importOutreachLeads(leads: Partial<CrmOutreachLead>[]): Promise<number> { ... }

export async function convertLeadToClient(leadId: string): Promise<CrmClient> { ... }

// ── Email Log ─────────────────────────────────────────────
export async function fetchEmailLog(leadId?: string): Promise<CrmEmailLog[]> { ... }

// ── Email API (calls FastAPI on VPS) ──────────────────────
const EMAIL_API = '/api/email';

export async function sendOutreachEmail(leadId: string, template: string): Promise<{ messageId: string }> { ... }

export async function sendBatchEmails(leadIds: string[], template: string): Promise<{ sent: number; failed: number }> { ... }

export async function previewEmail(lead: CrmOutreachLead, template: string): Promise<{ html: string; subject: string }> { ... }

export async function getEmailQuota(): Promise<{ sent_today: number; limit: number }> { ... }
```

---

## Gmail API Config

| Key | Value |
|-----|-------|
| Sender Email | `toan.dang@tdgamestudio.com` |
| Sender Name | `Tony Dang` |
| Google Cloud Project | `email-mkt-493813` |
| OAuth Client ID | `71850303483-9jhtla0ngbdkr9p87esfreohq6incs9b` |
| Token Path | `credentials/gmail_token.json` |
| Scopes | `gmail.send`, `gmail.readonly` |
| Rate Limit | 30 emails/day, 2-5min delay between |

## Logo URLs (R2 CDN)

| Logo | URL |
|------|-----|
| White (dark bg) | `https://pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev/logo/logo_td_white.png` |
| Black (light bg) | `https://pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev/logo/logo_td_black.png` |
| No text (icon) | `https://pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev/logo/logo_td_notext.png` |

## Lead Data Summary

- **Total enriched contacts**: 553
- **Unique studios (deduped)**: 131
- **Tier 1** (Art Director): 110
- **Tier 2** (Producer): 7
- **Tier 3** (CEO/Other): 5
- **Unranked**: 9
- **Data file**: `e:\TDC_App\TDGAMES_App\Client_Data\output\SalesQL_Enriched_Leads.csv`

## FastAPI Email Service (VPS)

Deploy at `/opt/td-mailer-api/` on Megahost_02 (180.93.144.98), port 8401.
Nginx proxy: `app.tdgamestudio.com/api/email/ → localhost:8401`

Key endpoints:
- `POST /api/email/send` — Send single email
- `POST /api/email/batch` — Batch send with rate limiting  
- `POST /api/email/preview` — Render template preview
- `GET /api/email/status` — Today's quota
- `POST /api/inbox/scan` — Check replies/bounces
