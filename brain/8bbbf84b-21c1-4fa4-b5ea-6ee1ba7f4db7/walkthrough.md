# CRM Email Outreach — Deployment Walkthrough

## Tổng kết

Đã triển khai thành công 3 tính năng bổ sung cho module CRM Email Outreach:

---

## ✅ Task 1: Import 553 Leads → Supabase

**Kết quả**: 456 leads (sau khi dedup theo email) đã được import vào `crm_outreach_leads`

| Tier | Count | Mô tả |
|------|-------|-------|
| ⭐ Tier 1 | **204** | Art Director, Outsource Manager — ưu tiên cao nhất |
| ★ Tier 2 | **32** | Lead Artist, Producer — ưu tiên trung bình |
| ☆ Tier 3 | **57** | CEO, Creative Director — ưu tiên thấp |
| Unranked | **163** | Các vị trí khác |
| **Total** | **456** | |

**Script**: [import_leads.js](file:///C:/Users/dangt/.gemini/antigravity/brain/8bbbf84b-21c1-4fa4-b5ea-6ee1ba7f4db7/scratch/import_leads.js) — Node.js script đọc `SalesQL_Enriched_Leads.csv`, dedup by email, import batch 50/lần qua Supabase REST API.

---

## ✅ Task 2: Send Email Button trên UI

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/EmailOutreach.tsx)

### Tính năng mới trên Leads Tab:

1. **Quota Bar** — Hiển thị real-time quota gửi email hôm nay (sent/limit/remaining), với progress bar màu adaptive (xanh → cam → đỏ)

2. **Nút "📧 Gửi Initial / FU1 / FU2"** — per-lead action button, tự detect bước tiếp theo:
   - `pending` → "Gửi Initial"
   - `initial_sent` → "Gửi FU1" 
   - `followup1_sent` → "Gửi FU2"
   - `followup2_sent` → không hiện nút

3. **Bulk Send** — "🚀 Gửi batch (N)" gửi hàng loạt cho tất cả leads pending, với:
   - Progress bar real-time
   - Counter success/failed
   - Auto-respect quota limit
   - Confirmation dialog trước khi gửi

4. **Column "Actions"** — thay thế column trống, hiển thị cả nút Send + Delete

---

## ✅ Task 3: Cron Auto Follow-up trên VPS

**File**: `/opt/td-mailer-api/cron_followup.py` — Python script chạy hàng ngày

### Logic:
- Quét `crm_outreach_leads` tìm leads đã gửi initial > 3 ngày → gửi `followup_1`
- Quét leads đã gửi followup_1 > 7 ngày → gửi `followup_2`
- Respect quota (30/ngày), random delay 30-90s giữa mỗi email
- Log chi tiết tại `/opt/td-mailer-api/logs/followup.log`

### Cron Schedule:
```
/etc/cron.d/td-mailer-followup
0 10 * * * root PYTHONPATH=/opt/td-mailer-api python3 /opt/td-mailer-api/cron_followup.py
```
→ Chạy mỗi ngày lúc **10:00 AM ICT**

### Dry-run test: ✅ Passed
```
Quota: 0/30 rem=30
--- followup_1: 0 due ---
--- followup_2: 0 due ---
Done: sent=0 fail=0
```
(0 due vì chưa ai được gửi initial)

---

## Trạng thái hệ thống hiện tại

| Component | Status |
|-----------|--------|
| FastAPI Backend | ✅ Running (18h uptime) trên `180.93.144.98:8401` |
| Supabase DB | ✅ 456 leads, 3 templates, 0 email logs |
| CRM Frontend | ✅ UI updated với Send button + Quota bar |
| Cron Follow-up | ✅ Installed, chạy 10:00 AM hàng ngày |
| Gmail API | ✅ Token valid, quota 30/ngày |

## Next Steps

1. **Bắt đầu warm-up**: Gửi 5 email/ngày trong tuần đầu, tăng dần lên 30/ngày
2. **Monitor**: Check `/opt/td-mailer-api/logs/followup.log` sau ngày đầu gửi
3. **Reply detection**: Cần thêm endpoint `/api/email/check-replies` để detect bounce/reply
