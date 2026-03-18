# Luồng Xin Nghỉ Phép — Task Checklist

- [x] **Database**: Migration tạo `leave_balances` + thêm cột `att_requests`
- [x] **Types**: Thêm `LeaveBalance` interface, cập nhật `AttRequest`
- [x] **Service**: Tạo `leaveService.ts` — balance calculation, CRUD, approval
- [x] **Portal UI**: Thêm tab "Nghỉ phép" trong `PortalApp.tsx`
- [x] **LeaveTab UI**: Tạo `LeaveTab.tsx` — balance card + form + lịch sử
- [x] **Admin UI**: Tạo `LeaveApproval.tsx` + tích hợp vào `AttendanceApp.tsx`
- [ ] **Browser Test**: Đăng nhập member → xin nghỉ → admin duyệt → check balance
