# TD Mailer API — Deployment Reference

## Quick Reference

| Key | Value |
|-----|-------|
| **VPS** | Megahost_02 (180.93.144.98) |
| **Port** | 8401 |
| **Path** | `/opt/td-mailer-api/` |
| **Service** | `td-mailer-api.service` |
| **Swagger** | `http://180.93.144.98:8401/docs` |
| **Health** | `http://180.93.144.98:8401/health` |

## File Structure

```
/opt/td-mailer-api/
├── app.py                     # FastAPI main + CORS
├── .env                       # API keys (chmod 600)
├── sent_log.csv               # Local send tracking
├── routes/
│   ├── __init__.py
│   ├── leads.py               # /api/leads/discover, /api/leads/enrich
│   └── email.py               # /api/email/send, /test, /preview, /status
├── services/
│   ├── __init__.py
│   ├── discovery.py           # Web scraping + Google CSE + SalesQL
│   ├── gmail_sender.py        # Gmail API send + rate limit
│   └── supabase_client.py     # Lead/Template/Log CRUD
├── credentials/
│   └── gmail_token.json       # Gmail OAuth (auto-refresh, chmod 600)
└── email_templates/           # (reserved for local template overrides)
```

## API Endpoints

### Lead Discovery
| Method | Endpoint | Body | Response |
|--------|----------|------|----------|
| POST | `/api/leads/discover` | `{"company": "...", "domain": "..."}` | `{"contacts": [...], "count": N}` |
| POST | `/api/leads/enrich` | `{"linkedin_url": "..."}` | `{"contact": {...}}` |

### Email Sending
| Method | Endpoint | Body | Response |
|--------|----------|------|----------|
| POST | `/api/email/send` | `{"lead_id": "uuid", "template_name": "initial_outreach"}` | `{"success": true, "message_id": "..."}` |
| POST | `/api/email/test` | `{"to_email": "...", "template_name": "..."}` | `{"success": true}` |
| POST | `/api/email/preview` | `{"template_name": "...", "contact_name": "...", "studio_name": "..."}` | `{"html": "...", "subject": "..."}` |
| GET | `/api/email/status` | — | `{"sent_today": N, "daily_limit": 30, "remaining": N}` |

## .env Configuration

```
SALESQL_API_KEY=8NAYAs5jqO22WqvgJltSSHPMRJJ53e1k
GOOGLE_API_KEY=AIzaSyA2U5gFXVha3B9fpBCp2gQp1C_bnLs5MVI
GOOGLE_CX_ID=80bd03fb209c243bd
SUPABASE_URL=https://fifuhkupaqcfjwyouwpa.supabase.co
SUPABASE_SERVICE_KEY=<anon key>
SENDER_EMAIL=toan.dang@tdgamestudio.com
SENDER_NAME=Tony Dang
DAILY_LIMIT=30
```

## Gmail OAuth

- **Sender**: `toan.dang@tdgamestudio.com`
- **Google Cloud Project**: `email-mkt-493813`
- **Client ID**: `71850303483-9jhtla0ngbdkr9p87esfreohq6incs9b`
- **Token**: `/opt/td-mailer-api/credentials/gmail_token.json`
- **Scopes**: `gmail.send`, `gmail.readonly`
- **Auto-refresh**: Yes (refresh_token stored)
- **Setup script** (if re-auth needed): `e:\...\Client_Data\setup_gmail_oauth.py`

## Supabase Tables

- **`crm_outreach_leads`** — Lead data (status tracking, tier, timestamps)
- **`crm_email_log`** — Sent email history (message_id, status)
- **`crm_email_templates`** — HTML templates + subject lines
- **RLS**: Open policies added via migration `add_anon_rls_outreach_tables`

## Systemd Management

```bash
systemctl status td-mailer-api      # Check status
systemctl restart td-mailer-api     # Restart after code changes
systemctl stop td-mailer-api        # Stop
journalctl -u td-mailer-api -f      # View live logs
```

## Frontend Connection

- **Env**: `VITE_OUTREACH_API_URL=http://180.93.144.98:8401` in `.env.local`
- **Service**: `apps/crm/services/outreachService.ts` (lines 194-216)
- **UI**: `apps/crm/components/EmailOutreach.tsx` — 4 tabs (Dashboard/Leads/Discovery/Templates)

## Firewall

```bash
ufw allow 8401/tcp    # Already done
```

## Ported From

| Original Script | → | API Service |
|----------------|---|-------------|
| `email_discovery_bot.py` (717 lines) | → | `services/discovery.py` (~180 lines) |
| `cold_email_sender.py` (501 lines) | → | `services/gmail_sender.py` (~115 lines) |

Core functions preserved: `scrape_general_emails()`, `search_linkedin_targets()`, `salesql_enrich()`, `get_title_tier()`, `get_gmail_service()`, `send_email()`, `personalize()`

## Next Steps (TODO)

1. **Import 553 leads** from `e:\...\output\SalesQL_Enriched_Leads.csv` → `crm_outreach_leads`
2. **Domain warm-up**: Start with 5 emails/day, ramp to 30 over 2 weeks
3. **Cron follow-ups**: Auto-send followup_1 (Day 3) + followup_2 (Day 7)
4. **Reply detection**: Scan Gmail inbox for replies (gmail.readonly scope ready)
5. **Bounce handling**: Track bounced emails, update lead status
