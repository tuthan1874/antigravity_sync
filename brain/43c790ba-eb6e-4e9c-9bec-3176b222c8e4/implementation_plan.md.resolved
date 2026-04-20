# Deploy FastAPI Email Outreach Backend → Megahost_02 VPS

## Mục tiêu

Triển khai FastAPI backend tại `/opt/td-mailer-api/` trên VPS Megahost_02 (180.93.144.98) port 8401. Backend xử lý 2 chức năng chính:
1. **Lead Discovery** — Web scraping + Google CSE + SalesQL enrichment
2. **Email Sending** — Gmail API qua `toan.dang@tdgamestudio.com`

Sau khi deploy, kết nối frontend CRM bằng `VITE_OUTREACH_API_URL`.

---

## User Review Required

> [!IMPORTANT]
> Gmail OAuth token hiện có sẵn tại local `e:\...\Client_Data\credentials\gmail_token.json`.
> Token này sẽ được upload lên VPS. Token có refresh_token nên sẽ tự động gia hạn.

> [!WARNING]
> API Keys sẽ được lưu trong `.env` trên VPS:
> - SalesQL: `8NAYAs5jqO22WqvgJltSSHPMRJJ53e1k`
> - Google CSE: `AIzaSyA2U5gFXVha3B9fpBCp2gQp1C_bnLs5MVI` / CX: `80bd03fb209c243bd`
> - Supabase service role key (để update leads từ backend)

> [!CAUTION]
> Port 8401 sẽ chỉ bind localhost — Nginx sẽ proxy `/api/outreach/` từ bên ngoài nếu cần.
> Hiện tại frontend gọi trực tiếp qua IP:port (cần CORS).

---

## Proposed Changes

### 1. VPS Backend — FastAPI App

#### [NEW] `/opt/td-mailer-api/app.py`
Main FastAPI application:
- CORS middleware cho `localhost:3000` + `app.tdgamestudio.com`
- Health check endpoint: `GET /health`
- Include routers: `leads`, `email`

#### [NEW] `/opt/td-mailer-api/routes/leads.py`
Lead Discovery endpoints:
- `POST /api/leads/discover` — Input: `{company, domain}` → Output: enriched contacts
  - Port logic từ `email_discovery_bot.py`: `scrape_general_emails()` + `search_linkedin_targets()` + `salesql_enrich()`
- `POST /api/leads/enrich` — Enrich single LinkedIn URL

#### [NEW] `/opt/td-mailer-api/routes/email.py`
Email Sending endpoints:
- `POST /api/email/send` — Gửi email cho 1 lead (from Supabase lead ID)
  - Port logic từ `cold_email_sender.py`: `get_gmail_service()` + `send_email()` + `personalize()`
- `POST /api/email/test` — Gửi test email
- `GET /api/email/status` — Today's quota (sent count / daily limit)
- `POST /api/email/preview` — Render template HTML với contact data

#### [NEW] `/opt/td-mailer-api/services/discovery.py`
Port core functions từ `email_discovery_bot.py`:
- `scrape_general_emails(domain)` → web scraping
- `search_linkedin_targets(studio_name)` → Google CSE
- `salesql_enrich(linkedin_url)` → SalesQL API
- `get_title_tier(job_title)` → tier classification
- Tier configs: TIER_1_TITLES, TIER_2_TITLES, TIER_3_TITLES

#### [NEW] `/opt/td-mailer-api/services/gmail_sender.py`
Port core functions từ `cold_email_sender.py`:
- `get_gmail_service()` → create Gmail API client from token
- `create_email()` → MIME message builder
- `send_email()` → Gmail API send
- `personalize()` → template variable replacement
- Rate limiting: 30/day, 2-5 min delay

#### [NEW] `/opt/td-mailer-api/services/supabase_client.py`
Supabase integration:
- Update `crm_outreach_leads.outreach_status` after send
- Insert `crm_email_log` entries
- Fetch `crm_email_templates` for rendering

#### [NEW] `/opt/td-mailer-api/requirements.txt`
```
fastapi>=0.110.0
uvicorn>=0.27.0
python-dotenv>=1.0.0
requests>=2.31.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
google-auth>=2.0.0
google-auth-oauthlib>=1.0.0
google-api-python-client>=2.0.0
supabase>=2.0.0
dnspython>=2.0.0
```

#### [NEW] `/opt/td-mailer-api/.env`
```
SALESQL_API_KEY=...
GOOGLE_API_KEY=...
GOOGLE_CX_ID=...
SUPABASE_URL=https://fifuhkupaqcfjwyouwpa.supabase.co
SUPABASE_SERVICE_KEY=...
SENDER_EMAIL=toan.dang@tdgamestudio.com
SENDER_NAME=Tony Dang
DAILY_LIMIT=30
```

#### [NEW] `/opt/td-mailer-api/credentials/gmail_token.json`
Upload from local `e:\...\Client_Data\credentials\gmail_token.json`

---

### 2. Systemd Service

#### [NEW] `/etc/systemd/system/td-mailer-api.service`
```ini
[Unit]
Description=TD Mailer API (FastAPI)
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/td-mailer-api
ExecStart=/usr/bin/python3 -m uvicorn app:app --host 127.0.0.1 --port 8401
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

---

### 3. Frontend Connection

#### [MODIFY] [.env.local](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/.env.local)
Add: `VITE_OUTREACH_API_URL=http://180.93.144.98:8401`

> [!NOTE]
> Frontend `outreachService.ts` đã có sẵn code gọi API (lines 194-216).
> Chỉ cần set env variable là Discovery + Send sẽ hoạt động.

---

## Execution Steps

| Step | Action | Est. Time |
|------|--------|-----------|
| 1 | Tạo `/opt/td-mailer-api/` directory structure trên VPS | 1 min |
| 2 | Install Python dependencies (pip) | 2 min |
| 3 | Write `app.py` + routes + services | 10 min |
| 4 | Upload Gmail token + `.env` | 1 min |
| 5 | Tạo + enable systemd service | 2 min |
| 6 | Test endpoints: health → discover → send | 3 min |
| 7 | Update frontend `.env.local` | 1 min |
| 8 | Browser test: Discovery tab + Send | 2 min |

**Total estimate: ~22 minutes**

---

## Verification Plan

### Automated Tests
1. `curl http://180.93.144.98:8401/health` → `{"status": "ok"}`
2. `curl -X POST .../api/leads/discover` with test data → returns contacts
3. `curl -X POST .../api/email/test` → sends test email
4. Browser test: CRM → Email Outreach → Discovery tab → search company

### Manual Verification
- Check `crm_email_log` table for sent records
- Check Gmail inbox for test email
- Verify systemd service restarts properly
