# Walkthrough — Task 1 & 2

## Task 1: Export Bảng Lương + Phiếu Lương ✅

### Đã triển khai
- **Excel Export** — `payrollExportService.ts`: export toàn bộ bảng lương + phiếu lương cá nhân
- **PaySlip UI** — `PaySlip.tsx`: phiếu lương A4 in được, có nút In/PDF + Excel
- **Rollback** — Nút "↩️ Huỷ xác nhận" để revert confirmed → draft
- **Tên công ty** — "TD GAMES COMPANY LIMITED"
- **Fix print**: compact layout vừa 1 trang A4

---

## Task 2: CEO Dashboard App ✅

### Files tạo mới
- [dashboardService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/dashboard/services/dashboardService.ts) — Query parallel 7 modules Supabase
- [DashboardApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/dashboard/components/DashboardApp.tsx) — UI Dashboard

### Files sửa
- [apps.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/config/apps.ts) — Thêm "📊 Dashboard" đầu danh sách
- [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx) — Route cho Dashboard app

### Dashboard hiển thị

| Row | Panel | Dữ liệu |
|-----|-------|----------|
| 1 | KPI Cards | Doanh thu Invoice, Tổng chi phí, Nhân sự, Quỹ lương |
| 2 | Detail Panels | Hoá đơn (paid/pending), Workforce (tasks), CRM (clients/projects) |
| 3 | Bottom Panels | Phòng ban & Nhân sự (headcount chart), Bảng lương gần nhất |

### Screenshot xác nhận

![CEO Dashboard](file:///C:/Users/dangt/.gemini/antigravity/brain/1d6489c0-fc5e-4e38-a07d-78777e4338ca/ceo_dashboard_full_view_1773826098664.png)

![Dashboard recording](file:///C:/Users/dangt/.gemini/antigravity/brain/1d6489c0-fc5e-4e38-a07d-78777e4338ca/dashboard_test_1773826034364.webp)
