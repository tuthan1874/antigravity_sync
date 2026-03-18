# Expense Dashboard + Upload Biên Lai — Walkthrough

## Summary

Thêm tab **Dashboard** vào module Expense với biểu đồ thống kê chi phí theo tháng và theo danh mục. Upload biên lai đã được xác nhận hoạt động sẵn.

## Changes Made

### [NEW] [ExpenseDashboard.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseDashboard.tsx)

Component Dashboard hoàn chỉnh, bao gồm:

| Section | Mô tả |
|---------|-------|
| **KPI Cards** | 4 cards: Chi VND tháng này (vs tháng trước %), Chi USD, Số giao dịch, % có biên lai |
| **Monthly Bar Chart** | 6 tháng gần nhất — bar chart thuần CSS với animation |
| **Category Breakdown** | Stacked bar + legend — phân bổ chi phí theo danh mục |
| **Top 5 Expenses** | 5 chi phí lớn nhất với receipt link |

> [!NOTE]
> Không thêm library mới — tất cả charts đều dùng CSS animations + inline styles.

---

### [MODIFY] [ExpenseApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseApp.tsx)

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseApp.tsx)

---

### [MODIFY] [useExpenseState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/hooks/useExpenseState.ts)

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/hooks/useExpenseState.ts)

---

## Upload Biên Lai — Already Working

Upload biên lai đã được build sẵn hoàn chỉnh:

- **Frontend**: `ExpenseForm.tsx` — drag/drop upload, preview ảnh/PDF, xoá file
- **Backend**: Edge function `r2-expense-upload` v16 đang active trên Supabase Workflow project
- **Storage**: Cloudflare R2 bucket, public URL: `pub-dad8a9bea8cb47c7ac0a03614d43b5b1.r2.dev`
- **DB column**: `expense_expenses.receipt_url` (text, nullable)

## Verification

| Test | Result |
|------|--------|
| `tsc --noEmit` | ✅ Pass — no errors |
| `vite build` | ✅ Pass — 148 modules, built in 1.74s |
| Browser test | ⏳ Browser subagent unavailable — manual test recommended |

### Manual Test Steps

1. `npm run dev` → open `http://localhost:3001/`
2. Login → click **Expense** card
3. Dashboard tab should load by default
4. Navigate between tabs: Dashboard → Danh sách → Định kỳ → Danh mục
5. Danh sách → + Thêm chi phí → chọn file upload biên lai
