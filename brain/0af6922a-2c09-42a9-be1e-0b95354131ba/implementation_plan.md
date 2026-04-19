# B2B Cold Email Outreach System — `toan.dang@tdgamestudio.com`

Xây dựng hệ thống gửi cold email tự động từ Google Workspace, tích hợp trực tiếp vào pipeline B2B Lead Discovery hiện có.

---

## Domain Health Audit

| Check | Status | Chi tiết |
|-------|--------|----------|
| **MX Record** | ✅ OK | `smtp.google.com` (Google Workspace) |
| **DKIM** | ✅ OK | RSA key configured at `google._domainkey.tdgamestudio.com` |
| **DMARC** | ⚠️ Weak | `p=none` — chỉ monitor, chưa enforce. Nên upgrade lên `p=quarantine` sau khi warm-up |
| **SPF** | ❌ Missing | **Chưa có SPF record!** Cần thêm ngay để tránh bị spam |
| **Brevo** | ℹ️ Linked | Domain đã verify với Brevo (Sendinblue) — có thể đã dùng trước đó |

> [!CAUTION]
> **SPF record bị thiếu** — đây là lý do hàng đầu khiến email vào spam. Cần thêm SPF record trước khi gửi bất kỳ email nào.

> [!IMPORTANT]
> **Action cần làm trước khi gửi email:**
> 1. Thêm SPF record: `v=spf1 include:_spf.google.com ~all`
> 2. Nâng DMARC từ `p=none` lên `p=quarantine` (sau 2 tuần warm-up)

---

## Proposed Solution: Gmail API + Python Script

### Tại sao Gmail API (không phải SMTP)?

| | Gmail API | SMTP (App Password) | Cold Email SaaS |
|---|-----------|-------------------|----|
| **Chi phí** | Miễn phí | Miễn phí | $50-150/tháng |
| **Rate limit** | 2,000 email/ngày | 500/ngày | Tùy plan |
| **Tracking** | Tự build (pixel/link) | Không có | Built-in |
| **Personalization** | Full control | Full control | Template-based |
| **Warm-up** | Manual | Manual | Tự động |
| **Deliverability** | Tốt (Google infra) | Tốt | Rất tốt |
| **Setup** | OAuth2 (1 lần) | Đơn giản nhất | SaaS config |

**→ Chọn Gmail API** vì: zero cost, rate limit cao nhất, full control, tích hợp trực tiếp với pipeline hiện tại.

---

## Proposed Changes

### Cold Email Sender Script

#### [NEW] `cold_email_sender.py`

Script chính để gửi cold email campaign:

**Chức năng:**
- Đọc leads từ `output/SalesQL_Enriched_Leads.csv` hoặc `TD_Games_B2B_Leads.xlsx`
- Template engine với personalization (tên, studio, tier, title)
- Rate limiting: mặc định 30 email/ngày (có thể tăng dần)
- Tracking sent emails (tránh gửi trùng)
- Follow-up sequence (Day 3, Day 7)
- Dry-run mode để preview trước khi gửi thật

**Email Selection Logic:**
```
Priority: Work_Email > Personal_Email
Tier priority: Tier 1 > Tier 2 > Tier 3 > Unranked
Max 1 contact per studio (người có Tier cao nhất + Work email)
```

**Rate Limiting Strategy:**
```
Week 1: 10 emails/ngày (warm-up)
Week 2: 20 emails/ngày
Week 3+: 30-50 emails/ngày
Gửi cách nhau 2-5 phút (random delay)
Chỉ gửi 9AM-5PM EST (giờ làm việc Mỹ/EU)
```

---

#### [NEW] `email_templates/`

Thư mục chứa email templates:

##### `initial_outreach.html`
Template email đầu tiên — giới thiệu TD Games outsource services.

**Personalization variables:**
- `{contact_name}` — Tên người nhận
- `{studio_name}` — Tên studio
- `{job_title}` — Chức danh
- `{service_hook}` — Hook dựa trên Tier (Art Director → "art pipeline", Producer → "production capacity")

##### `followup_1.html` (Day 3)
Follow-up nhẹ nhàng — "just checking in"

##### `followup_2.html` (Day 7)
Follow-up cuối — case study / portfolio link

---

#### [NEW] `output/sent_emails_log.csv`

File log tracking emails đã gửi:

| Column | Description |
|--------|-------------|
| `timestamp` | Thời gian gửi |
| `to_email` | Email người nhận |
| `contact_name` | Tên contact |
| `studio` | Tên studio |
| `template` | initial / followup_1 / followup_2 |
| `status` | sent / failed / bounced |
| `message_id` | Gmail Message ID (để tracking) |

---

#### [NEW] `setup_gmail_oauth.py`

Script 1 lần để setup OAuth2 cho Gmail API:
- Tạo credentials từ Google Cloud Console
- Authorize `toan.dang@tdgamestudio.com`
- Lưu token vào `credentials/gmail_token.json`

---

### DNS Fix (Manual)

#### SPF Record
Cần thêm TXT record vào DNS của `tdgamestudio.com`:
```
Type: TXT
Host: @
Value: v=spf1 include:_spf.google.com ~all
```

---

## Open Questions

> [!IMPORTANT]
> **1. Google Cloud Project**: Bạn muốn dùng Google Cloud Project nào cho Gmail API?
> - Project hiện có (`open-493116` — đã setup cho GOG)?
> - Hay tạo project mới riêng cho cold email?

> [!IMPORTANT]  
> **2. Email content**: Bạn đã có nội dung email template chưa? Hay cần tôi draft nội dung tiếng Anh cho outsource services pitch?

> [!WARNING]
> **3. SPF Record**: Bạn có access vào DNS management của `tdgamestudio.com` không? (Cần thêm SPF record trước khi bắt đầu gửi)

> [!IMPORTANT]
> **4. Warm-up**: Domain `tdgamestudio.com` đã từng gửi email outreach trước đó chưa? (Ảnh hưởng đến tốc độ warm-up)

---

## Verification Plan

### Automated Tests
1. **Dry-run mode**: Chạy script không gửi thật, chỉ print preview
2. **Test email**: Gửi 1 email test tới `toan.dang@tdgamestudio.com` (tự gửi cho mình)
3. **SPF/DKIM check**: Verify email headers đầy đủ authentication

### Manual Verification
1. Kiểm tra email không vào Spam folder
2. Review email rendering trên Gmail, Outlook
3. Confirm tracking log ghi đúng
