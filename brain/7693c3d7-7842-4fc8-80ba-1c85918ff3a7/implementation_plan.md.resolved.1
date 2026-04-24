# Chuẩn hóa Tên: TD Games Platform

## Mục tiêu
Đổi tất cả references từ "Invoice App / Billing App" → **"TD Games Platform"** để phản ánh đúng bản chất là **platform tổng hợp** của TD Games.

## Naming Convention đề xuất

| Component | Tên cũ | Tên mới |
|---|---|---|
| **Project name** | `td-games-invoice-generator` | `tdgames-platform` |
| **Folder** | `td-games-invoice-app` | `tdgames-platform` |
| **GitHub repo** | `tdgamesvn/tdgames_billing` | `tdgamesvn/tdgames-platform` |
| **Browser title** | "TD Games - Invoice Generator" | "TD Games Platform" |
| **Login heading** | "TD Games Billing" | "TD Games Platform" |
| **Footer** | "Enterprise Billing Engine" | "Enterprise Platform" |
| **Edge Function** | `billing-report` | `platform-data` |
| **MCP Plugin** | `billing-data` | `platform-data` |
| **MCP Tool names** | `get_billing_overview` | `get_platform_overview` |

---

## Proposed Changes

### Layer 1: Local Project Files

#### [MODIFY] [package.json](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/package.json)
```diff
-"name": "td-games-invoice-generator",
+"name": "tdgames-platform",
```

#### [MODIFY] [index.html](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/index.html)
```diff
-<title>TD Games - Invoice Generator</title>
+<title>TD Games Platform</title>
```

#### [MODIFY] [metadata.json](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/metadata.json)
```diff
-"name": "TD Games Invoice Generator",
-"description": "A high-performance, premium invoice generation tool..."
+"name": "TD Games Platform",
+"description": "Enterprise management platform for TD Games Studio — including Invoice, HR, Payroll, CRM, Workforce, Expense, and more."
```

#### [MODIFY] [LoginScreen.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/LoginScreen.tsx)
```diff
-TD Games Billing
+TD Games Platform
```

#### [MODIFY] App Footers (6 files)
Đổi `"Enterprise Billing Engine"` → `"Enterprise Platform"` trong:
- `InvoiceApp.tsx`
- `HrApp.tsx`
- `ExpenseApp.tsx`
- `CrmApp.tsx`
- `WorkforceApp.tsx`
- `Navbar.tsx` (fallback text)

---

### Layer 2: GitHub Repository

#### Rename repo: `tdgames_billing` → `tdgames-platform`
- Thực hiện trên GitHub Settings → Rename
- GitHub tự động redirect URL cũ → mới
- Cập nhật git remote local

> [!WARNING]
> **Ảnh hưởng:** Mọi link cũ vẫn hoạt động (GitHub redirect). Nhưng cần update git remote trên mọi máy dev.

---

### Layer 3: Supabase Edge Function

#### [NEW] `supabase/functions/platform-data/index.ts`
- Copy nội dung từ `billing-report/index.ts`
- Deploy Edge Function mới `platform-data`
- Giữ Edge Function cũ `billing-report` tạm thời (backward compatible)

> [!NOTE]
> Không cần xóa `billing-report` ngay — có thể chạy song song rồi retire sau.

---

### Layer 4: OpenClaw (VPS Megahost_02)

#### MCP Plugin: Rename `billing-data` → `platform-data`
- Rename folder `/root/.openclaw/mcp-servers/billing-data/` → `platform-data/`
- Cập nhật `package.json` name
- Cập nhật `index.mjs` — đổi URL Edge Function sang `platform-data`
- Cập nhật OpenClaw config: `openclaw mcp unset billing-data` + `openclaw mcp set platform-data ...`

#### Tool names: `get_billing_overview` → `get_platform_overview`
- Đổi tên tool trong MCP plugin
- Cập nhật SOUL.md của tất cả 5 agents

#### Agent SOUL.md updates (5 files)
- Thay thế "billing" → "platform" trong tất cả workspace SOUL.md

---

## User Review Required

> [!IMPORTANT]
> **Tên repo GitHub:** Bạn muốn đổi thành `tdgames-platform` hay tên khác? Tôi có thể rename trực tiếp trên GitHub nếu bạn cung cấp quyền, hoặc bạn tự rename.

> [!IMPORTANT]
> **Folder local:** Đổi folder `td-games-invoice-app` → `tdgames-platform` trên máy bạn sẽ cần close IDE trước. Bạn muốn đổi ngay hay giữ folder cũ?

> [!NOTE]
> **MCP Tool names:** Đổi `get_billing_overview` → `get_platform_overview` chỉ ảnh hưởng tên nội bộ, agents sẽ tự adapt. Không có risk.

## Verification Plan

### Automated Tests
1. Chạy `npm run dev` sau khi đổi tên — verify app hoạt động bình thường
2. Test Edge Function `platform-data` mới bằng curl
3. Test OpenClaw agent gọi tool mới
4. Verify git push/pull hoạt động với remote mới

### Manual Verification
1. Kiểm tra browser tab title = "TD Games Platform"
2. Kiểm tra Login screen heading
3. Nhắn Telegram bot CEO — confirm vẫn trả data đúng
