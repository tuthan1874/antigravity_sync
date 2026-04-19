# DNS Setup Tối Ưu — `tdgamestudio.com`

> Mục tiêu: Đạt **10/10 điểm email authentication** để cold email không rơi vào spam.

## Tình trạng hiện tại vs Cần làm

| # | Record | Hiện tại | Cần làm | Tác dụng |
|---|--------|----------|---------|----------|
| 1 | **SPF** | ❌ Thiếu | 🔴 Thêm ngay | Xác nhận Google có quyền gửi email |
| 2 | **DKIM** | ✅ OK | Không cần | Chữ ký số cho mỗi email |
| 3 | **DMARC** | ⚠️ `p=none` | 🟡 Upgrade | Chính sách xử lý email giả mạo |
| 4 | **MTA-STS** | ❌ Thiếu | 🟢 Thêm | Bắt buộc mã hóa TLS khi gửi/nhận |
| 5 | **TLS-RPT** | ❌ Thiếu | 🟢 Thêm | Báo cáo lỗi TLS |
| 6 | **BIMI** | ❌ Thiếu | 🟢 Thêm | Hiện logo TD Games trong inbox |
| 7 | **MX** | ✅ OK | Không cần | Mail routing |

---

## Records cần thêm trên VietNIX DNS Panel

Đăng nhập VietNIX → **DNS Zone Editor** → `tdgamestudio.com`

---

### 🔴 Record 1: SPF (BẮT BUỘC — làm đầu tiên)

| Field | Value |
|-------|-------|
| **Type** | `TXT` |
| **Host** | `@` (hoặc để trống) |
| **Value** | `v=spf1 include:_spf.google.com ~all` |
| **TTL** | `3600` |

> [!CAUTION]
> **Không có SPF = Gmail, Outlook sẽ đánh dấu spam.** Đây là record quan trọng nhất.

**Tại sao?** SPF nói với mail server nhận rằng: "Chỉ Google Workspace mới được phép gửi email từ @tdgamestudio.com"

---

### 🟡 Record 2: DMARC (Upgrade)

**Xóa** DMARC record cũ (`v=DMARC1; p=none; rua=mailto:rua@dmarc.brevo.com`) và **thay bằng**:

| Field | Value |
|-------|-------|
| **Type** | `TXT` |
| **Host** | `_dmarc` |
| **Value** | `v=DMARC1; p=quarantine; rua=mailto:toan.dang@tdgamestudio.com; ruf=mailto:toan.dang@tdgamestudio.com; fo=1; pct=100` |
| **TTL** | `3600` |

**Giải thích:**
- `p=quarantine` — email không pass SPF/DKIM → vào spam (thay vì `none` = bỏ qua)
- `rua=` — nhận report tổng hợp hàng ngày về email authentication
- `ruf=` — nhận report chi tiết khi có email fail
- `fo=1` — report cho MỌI trường hợp fail (không chỉ SPF+DKIM đều fail)
- `pct=100` — áp dụng cho 100% email

---

### 🟢 Record 3: MTA-STS (Bảo mật TLS)

Cần **2 bước**:

#### Bước 3a: DNS Record

| Field | Value |
|-------|-------|
| **Type** | `TXT` |
| **Host** | `_mta-sts` |
| **Value** | `v=STSv1; id=20260419` |
| **TTL** | `3600` |

#### Bước 3b: File policy (host trên web)

Cần file tại URL: `https://mta-sts.tdgamestudio.com/.well-known/mta-sts.txt`

Nội dung file:
```
version: STSv1
mode: testing
mx: smtp.google.com
max_age: 604800
```

> [!NOTE]
> MTA-STS yêu cầu host 1 file trên subdomain `mta-sts.tdgamestudio.com` qua HTTPS. Nếu domain chưa có hosting cho subdomain này, có thể **bỏ qua record 3** — nó là "nice to have", không bắt buộc.

---

### 🟢 Record 4: TLS-RPT (Báo cáo TLS)

| Field | Value |
|-------|-------|
| **Type** | `TXT` |
| **Host** | `_smtp._tls` |
| **Value** | `v=TLSRPTv1; rua=mailto:toan.dang@tdgamestudio.com` |
| **TTL** | `3600` |

**Tại sao?** Nhận report khi kết nối TLS bị lỗi khi gửi/nhận email. Giúp monitor deliverability.

---

### 🟢 Record 5: BIMI (Logo trong Inbox)

| Field | Value |
|-------|-------|
| **Type** | `TXT` |
| **Host** | `default._bimi` |
| **Value** | `v=BIMI1; l=https://tdgamestudio.com/logo.svg` |
| **TTL** | `3600` |

**Yêu cầu:**
- File logo SVG phải ở URL public HTTPS
- Logo nên là file SVG Tiny PS format (vuông, không có text)
- DMARC phải ở `p=quarantine` hoặc `p=reject`

> [!TIP]
> BIMI hiển thị logo TD Games ngay trong inbox Gmail/Yahoo. Tăng trust → tăng open rate đáng kể cho cold email.

**Nếu chưa có logo SVG sẵn**, có thể bỏ qua record này và thêm sau.

---

## Tóm tắt — Copy paste vào VietNIX

### Records BẮT BUỘC (làm ngay):

```
# 1. SPF
Type: TXT | Host: @     | Value: v=spf1 include:_spf.google.com ~all

# 2. DMARC (thay thế record cũ)
Type: TXT | Host: _dmarc | Value: v=DMARC1; p=quarantine; rua=mailto:toan.dang@tdgamestudio.com; ruf=mailto:toan.dang@tdgamestudio.com; fo=1; pct=100

# 3. TLS-RPT
Type: TXT | Host: _smtp._tls | Value: v=TLSRPTv1; rua=mailto:toan.dang@tdgamestudio.com
```

### Records TÙY CHỌN (thêm khi sẵn sàng):

```
# 4. BIMI (cần có logo SVG trên website)
Type: TXT | Host: default._bimi | Value: v=BIMI1; l=https://tdgamestudio.com/logo.svg

# 5. MTA-STS (cần host file trên subdomain)
Type: TXT | Host: _mta-sts | Value: v=STSv1; id=20260419
```

---

## Sau khi thêm records — Verify

Đợi 15-30 phút để DNS propagate, rồi báo cho tôi. Tôi sẽ chạy verify tự động:

```bash
# SPF check
nslookup -type=TXT tdgamestudio.com 8.8.8.8

# DMARC check  
nslookup -type=TXT _dmarc.tdgamestudio.com 8.8.8.8

# Full test
# → https://mxtoolbox.com/SuperTool.aspx?action=mx:tdgamestudio.com
```
