# Task: Invoice App Feature Additions

## Features
1. [ ] **Xoá Invoice trong History** – thêm nút xoá + hàm `deleteInvoiceFromCloud` trong `nocodbService.ts`
2. [ ] **Filter History & Dashboard** – filter theo Studio, Khách hàng, khoảng ngày
3. [ ] **Save-after-export Popup** – bỏ auto-save khi export PDF, thay bằng dialog YES/NO sau khi export xong

## nocodbService.ts
- [ ] Thêm `deleteInvoiceFromCloud(id: string)` 

## App.tsx – State & Logic
- [ ] Import `deleteInvoiceFromCloud`
- [ ] State: `showSaveConfirm`, `pendingInvoiceToSave` cho popup save
- [ ] State: `historyFilter` (studio, client, dateFrom, dateTo)
- [ ] Handler `handleDeleteInvoice(id)`
- [ ] Sửa `handleExport` – bỏ auto-save, sau khi export xong set state show popup
- [ ] Handler `handleConfirmSave` (YES – save & dismiss) / `handleDismissSave` (NO – dismiss)
- [ ] Computed `filteredHistory` dùng cho History và Dashboard

## App.tsx – UI
- [ ] **History**: thêm filter bar (Studio, Khách hàng, Date range) phía trên grid
- [ ] **History**: thêm nút delete (trash icon) trên mỗi card
- [ ] **Dashboard**: thêm filter bar, tính toán KPI dựa trên `filteredHistory`
- [ ] **Popup** save confirmation modal (overlay)

## Verification
- [ ] Xoá invoice từ History → card biến mất, verify xoá trên NocoDB
- [ ] Filter theo studio/khách hàng → chỉ hiện invoice đúng
- [ ] Filter theo date range → chỉ hiện invoice trong khoảng
- [ ] Export PDF → popup hiện ra → YES lưu, NO không lưu
