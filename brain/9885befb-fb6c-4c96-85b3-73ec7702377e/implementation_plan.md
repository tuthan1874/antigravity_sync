# Expense Dashboard + Upload Biên Lai

## Summary

Thêm tab **Dashboard** vào module Expense với biểu đồ thống kê chi phí theo tháng và theo danh mục. Upload biên lai đã được build sẵn trong `ExpenseForm.tsx` (sử dụng R2 edge function đã deploy) — chỉ cần verify hoạt động.

## Current State

- ✅ **Receipt upload**: Đã hoàn chỉnh trong `ExpenseForm.tsx` (R2 upload, preview, delete)
- ✅ **R2 edge function**: `r2-expense-upload` đã deploy v16 trên Workflow project
- ✅ **DB schema**: `expense_expenses`, `expense_categories`, `expense_recurring` đều tồn tại
- ❌ **Dashboard tab**: Chưa có — cần tạo mới

## Proposed Changes

### Expense Dashboard Component

#### [NEW] [ExpenseDashboard.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseDashboard.tsx)

Component Dashboard thống kê chi phí, sử dụng **pure CSS/SVG** charts (không thêm dependency mới). Bao gồm:

1. **KPI Cards Row** (consistent with existing ExpenseList cards):
   - Tổng chi VND tháng hiện tại
   - Tổng chi USD tháng hiện tại
   - Số giao dịch tháng hiện tại
   - So sánh % vs tháng trước

2. **Monthly Bar Chart** (6 tháng gần nhất):
   - Bar chart thuần CSS (horizontal bars) hiển thị tổng chi phí VND mỗi tháng
   - Animated bars on load
   - Tooltip hiển thị số liệu

3. **Category Breakdown** (Donut chart / stacked bar):
   - Phân bổ chi phí theo danh mục (dùng category color)
   - Hiển thị % và số tiền cho mỗi danh mục
   - Legend bên cạnh

4. **Top Expenses Table**:
   - 5 chi phí lớn nhất trong kỳ
   - Hiển thị receipt icon nếu có biên lai đính kèm

5. **Receipt Coverage Stat**:
   - % giao dịch có đính kèm biên lai (receipt_url không rỗng)
   - Khuyến khích kế toán upload biên lai

---

### Navigation Updates

#### [MODIFY] [ExpenseApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseApp.tsx)

- Thêm `'dashboard'` vào `TAB_MAP`, `TAB_LABELS`, `REVERSE_TAB`
- Render `ExpenseDashboard` khi `activeTab === 'dashboard'`
- Dashboard là tab mặc định khi mở Expense app

#### [MODIFY] [useExpenseState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/hooks/useExpenseState.ts)

- Thêm `'dashboard'` vào `ExpenseTab` type
- Thêm `'dashboard'` vào `VALID_TABS`
- Đổi default tab thành `'dashboard'`

## Verification Plan

### Automated / Browser Tests

1. Chạy `npm run dev` từ thư mục project
2. Mở browser tại `http://localhost:5173`
3. Đăng nhập và vào Expense app
4. Verify:
   - Dashboard tab hiển thị mặc định khi vào app
   - Charts render đúng (dù 0 records cũng hiển thị empty state)
   - Navigation giữa Dashboard ↔ Danh sách ↔ Định kỳ ↔ Danh mục hoạt động
   - Upload biên lai khi tạo/edit chi phí: chọn file → upload → preview hiển thị → save → record có receipt_url
