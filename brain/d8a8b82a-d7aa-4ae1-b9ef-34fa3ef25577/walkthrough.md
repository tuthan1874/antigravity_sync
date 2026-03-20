# Fix Invite Flow + Profile Tab — Walkthrough

## Issue 1: SetPasswordScreen không hiện khi accept invite ✅ FIXED

### Root Cause
Supabase sử dụng **PKCE flow** (mặc định), khi user click invite link:
- Supabase redirect tới `https://app.tdgamestudio.com?code=<auth_code>` (query param)
- Code cũ check `window.location.hash` cho `#type=invite` → **hash trống** → không detect được

### Fix
render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)

Logic mới:
1. Detect `?code=` trong URL khi app mount
2. Khi `onAuthStateChange` fire `SIGNED_IN` + có `?code=` → check `user.invited_at`
3. Nếu user vừa được invite (trong 5 phút) → hiện `SetPasswordScreen`
4. Sau khi set password xong → auto-redirect tới Portal (cho role `member`)

---

## Issue 2: Tab Hồ sơ bị ẩn ✅ FIXED

### Root Cause
- Navbar tab container không có `overflow-x-auto` → tab thứ 5 bị cắt trên màn hình hẹp
- Type union của `accessibleTabs` quá hẹp, không include `'tasks'` cho Portal

### Fix
render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/components/Navbar.tsx)

- Added `overflow-x-auto scrollbar-hide` cho tab container
- Added `flex-shrink-0 whitespace-nowrap` cho tab buttons
- Expanded type union to accept `string` (future-proof)

---

## Issue 3: Email invite vào thư rác ⚠️ CẦN ACTION

### Root Cause
Email template mặc định của Supabase rất generic:
> "You have been invited to create a user on https://app.tdgamestudio.com"

→ Spam filter đánh dấu là spam vì thiếu branding, domain mới.

### Cần làm (thủ công)
Anh vào **Supabase Dashboard** → **Authentication** → **Email Templates** → tab **Invite User**, thay template bằng:

**Subject**: `TD Games Studio — Lời mời tham gia hệ thống`

**Body (HTML)**:
```html
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 520px; margin: 0 auto; padding: 40px 24px; background: #0F0F0F; color: #ffffff;">
  <div style="text-align: center; margin-bottom: 32px;">
    <h1 style="font-size: 24px; font-weight: 800; color: #FF9500; margin: 0;">TD GAMES STUDIO</h1>
    <p style="font-size: 12px; color: #9D9C9D; letter-spacing: 2px; text-transform: uppercase; margin-top: 4px;">HỆ THỐNG QUẢN LÝ NỘI BỘ</p>
  </div>
  <div style="background: #1A1A1A; border-radius: 16px; padding: 32px; border: 1px solid rgba(255,149,0,0.15);">
    <h2 style="font-size: 18px; color: #ffffff; margin: 0 0 16px;">Chào mừng bạn!</h2>
    <p style="color: #CCCCCC; font-size: 14px; line-height: 1.6; margin: 0 0 24px;">
      Bạn đã được mời tham gia hệ thống quản lý nội bộ TD Games Studio. Nhấn nút bên dưới để thiết lập tài khoản của bạn.
    </p>
    <div style="text-align: center; margin: 24px 0;">
      <a href="{{ .ConfirmationURL }}" style="display: inline-block; background: #FF9500; color: #000000; font-weight: 800; font-size: 14px; padding: 14px 40px; border-radius: 999px; text-decoration: none; letter-spacing: 1px; text-transform: uppercase;">
        Chấp nhận lời mời
      </a>
    </div>
    <p style="color: #666666; font-size: 12px; text-align: center; margin: 16px 0 0;">
      Nếu nút không hoạt động, copy link này vào trình duyệt:<br/>
      <span style="color: #FF9500; word-break: break-all;">{{ .ConfirmationURL }}</span>
    </p>
  </div>
  <p style="color: #444444; font-size: 11px; text-align: center; margin-top: 24px;">
    © 2026 TD Games Studio. Email này được gửi tự động.
  </p>
</div>
```

> [!TIP]
> Ngoài ra có thể xem xét bật **DKIM/SPF** cho domain `tdgamestudio.com` với Resend để tăng deliverability.

---

## Build Status
- ✅ TypeScript build passes (exit code 0)
- ✅ Dev server running
