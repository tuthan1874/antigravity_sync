# Payroll App — Walkthrough

## Tổng quan

Đã build xong app **Tính lương** hoàn chỉnh, implement đúng 8 bước trong `tinh_luong.md`.

## Các file đã tạo/sửa

| File | Mô tả |
|------|--------|
| `pay_payroll_sheets` + `pay_payroll_records` | 2 bảng DB mới (Supabase migration) |
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) | Thêm `PayPayrollSheet`, `PayPayrollRecord` |
| [payrollService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/payroll/services/payrollService.ts) | 8-step `calculatePayroll`, CRUD, auto-populate |
| [usePayrollState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/payroll/hooks/usePayrollState.ts) | State management hook |
| [PayrollApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/payroll/components/PayrollApp.tsx) | App shell + sheets list |
| [PayrollSheet.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/payroll/components/PayrollSheet.tsx) | Detail table + expandable 8-step view |
| [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx) | Added `payroll` route |
| [apps.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/config/apps.ts) | Added 💵 Tính lương card |

## Data Flow

- **Tạo bảng lương** → auto lấy NV fulltime từ HR + salary từ `hr_employee_salary` + ngày công & OT hours từ `att_monthly_records` + NPT từ `hr_dependents`
- **Tăng ca phát sinh**: `ot_hours` (giờ) → tự tính tiền = Lương giờ × 150% × hours
- **Inline edit**: Sửa ngày công hoặc OT phát sinh → tự recalculate toàn bộ

## Kết quả verified

### Bảng lương Tháng 3/2026

![Payroll calculation result](C:/Users/dangt/.gemini/antigravity/brain/7d989d6e-61b5-480b-bb45-0ff57a7db046/payroll_calculation_result_1773682394274.png)

### Chi tiết 8 bước tính lương

![Payroll detail view](C:/Users/dangt/.gemini/antigravity/brain/7d989d6e-61b5-480b-bb45-0ff57a7db046/payroll_detailed_view_1773682417433.png)

### Xác minh con số

| Khoản | Giá trị | Đúng? |
|-------|---------|-------|
| Ngày công | 20.56/22 (từ monthly sheet) | ✅ |
| Gross tham chiếu | 20,000,000đ | ✅ |
| TC phát sinh | 5h → 226,278đ | ✅ |
| Gross thực tế | 18,917,186đ | ✅ |
| BH NV (10.5%) | 521,056đ | ✅ |
| Thuế TNCN | 0đ (TNTT âm) | ✅ |
| Net thực lĩnh | **18,396,130đ** | ✅ |
| Chi phí công ty | 19,984,110đ | ✅ |

![Browser recording](C:/Users/dangt/.gemini/antigravity/brain/7d989d6e-61b5-480b-bb45-0ff57a7db046/verify_payroll_fixed_1773682335851.webp)
