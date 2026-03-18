# Luồng Xin Nghỉ Phép — Task Checklist

- [ ] **Database**: Migration tạo `leave_balances` + thêm cột `att_requests`
- [ ] **Types**: Thêm `LeaveBalance` interface, cập nhật `AttRequest`
- [ ] **Service**: Tạo `leaveService.ts` — balance calculation, CRUD, approval
- [ ] **Portal UI**: Thêm tab "Nghỉ phép" trong `PortalApp.tsx`
- [ ] **LeaveTab UI**: Tạo `LeaveTab.tsx` — balance card + form + lịch sử
- [ ] **Admin UI**: Tạo `LeaveApproval.tsx` + tích hợp vào `AttendanceApp.tsx`
- [ ] **Browser Test**: Đăng nhập member → xin nghỉ → admin duyệt → check balance
