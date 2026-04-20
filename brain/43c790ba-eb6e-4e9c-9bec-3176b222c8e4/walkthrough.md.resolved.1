# ✅ Deploy Hoàn Thành — FastAPI Email Outreach Backend

## Kết Quả

FastAPI backend đã được triển khai thành công lên VPS Megahost_02 và kết nối với frontend CRM.

### Screenshot — Lead Discovery hoạt động trên browser

![Lead Discovery Results — 5 contacts found from Supercell with tier ranking](C:\Users\dangt\.gemini\antigravity\brain\43c790ba-eb6e-4e9c-9bec-3176b222c8e4\lead_discovery_results_1776618872088.png)

### Recording — Full Discovery Flow

![Browser recording of testing CRM Discovery tab](C:\Users\dangt\.gemini\antigravity\brain\43c790ba-eb6e-4e9c-9bec-3176b222c8e4\discovery_final_test_1776618763053.webp)

---

## Những gì đã làm

### 1. VPS Backend (`/opt/td-mailer-api/`)

| File | Mô tả | Lines |
|------|--------|-------|
| `app.py` | FastAPI main + CORS | ~35 |
| `routes/leads.py` | `/api/leads/discover`, `/api/leads/enrich` | ~45 |
| `routes/email.py` | `/api/email/send`, `/test`, `/preview`, `/status` | ~120 |
| `services/discovery.py` | Web scraping + Google CSE + SalesQL (ported) | ~180 |
| `services/gmail_sender.py` | Gmail API send + rate limit (ported) | ~115 |
| `services/supabase_client.py` | Lead/Template/Log CRUD | ~55 |
| `.env` | API keys (SalesQL, Google CSE, Supabase) | ✅ |
| `credentials/gmail_token.json` | Gmail OAuth token | ✅ |

### 2. Systemd Service
- **Name:** `td-mailer-api.service`
- **Status:** ✅ Active (running), enabled for auto-start
- **Bind:** `0.0.0.0:8401`
- **Firewall:** UFW rule added for port 8401

### 3. Supabase
- **Migration:** `add_anon_rls_outreach_tables` — allows backend access
- **Tables verified:** `crm_outreach_leads` (2), `crm_email_templates` (3), `crm_email_log` (0)

### 4. Frontend
- **`.env.local`** → Added `VITE_OUTREACH_API_URL=http://180.93.144.98:8401`
- **Dev server** restarted to pick up new env

---

## API Endpoints Verified

| Endpoint | Method | Result |
|----------|--------|--------|
| `/health` | GET | `{"status":"ok"}` ✅ |
| `/api/email/status` | GET | `{"sent_today":0,"daily_limit":30,"remaining":30}` ✅ |
| `/api/leads/discover` | POST | Found 5 contacts from Supercell (2x Tier 1, 1x Tier 2, 2x Tier 3) ✅ |
| `/docs` | GET | FastAPI Swagger UI ✅ |

---

## Discovery Test Results (Supercell)

| Tier | Name | Title | Email |
|------|------|-------|-------|
| ⭐ Tier 1 | John "Cip" Cipriani | Art Director & Creative Director | john.cipriani@supercell.com |
| ⭐ Tier 1 | Mario Manzanares | Art Director | hello@mariomanzanares.com |
| ★ Tier 2 | Kalvin Lyle | Art Lead | kalvin.lyle@fullmoonmail.com |
| ☆ Tier 3 | Chris Bancroft | Reality Distortion Specialist | christopher.bancroft@supercell.com |
| ☆ Tier 3 | Fernanda Oliveira | Game Artist | fernanda.oliveira@supercell.com |

---

## Tiếp theo có thể làm

- [ ] Import 553 leads từ CSV vào `crm_outreach_leads`
- [ ] Bắt đầu domain warm-up cho `toan.dang@tdgamestudio.com`
- [ ] Thêm cron job auto follow-up (Day 3 + Day 7)
- [ ] Setup reply/bounce detection
