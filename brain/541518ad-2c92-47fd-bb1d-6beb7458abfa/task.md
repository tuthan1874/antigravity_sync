# Task: Client Management + Dashboard

## NocoDB Schema
- [ ] Tạo bảng Clients (name, address, contactPerson, email)
- [ ] Thêm cột paidDate vào bảng Invoices

## nocodbService.ts
- [ ] CRUD Clients (fetch, save, update)
- [ ] Update saveInvoiceToCloud để lưu kèm client info
- [ ] updatePaidDate khi toggle status → paid

## App.tsx — Client Details
- [ ] State + load danh sách clients
- [ ] Dropdown chọn client có sẵn
- [ ] Nút "Save Client" lưu client hiện tại lên NocoDB
- [ ] Auto-fill form khi chọn client

## App.tsx — Export Auto-Save
- [ ] Auto saveInvoiceToCloud khi export PDF/PNG/Excel/Word

## App.tsx — Dashboard Tab
- [ ] Tab mới "dashboard"
- [ ] Revenue chart per client (simple cards)
- [ ] Danh sách pending invoices
- [ ] Hiển thị paidDate khi đã thanh toán
