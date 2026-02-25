# PM Task Management System - Task Checklist

## Planning
- [x] Phân tích cấu trúc NocoDB hiện tại (TD_Games base)
- [x] Đọc spec Hệ thống Workflow Automation
- [x] Cập nhật implementation plan tích hợp dữ liệu
- [ ] Nhận approval từ PM/user

## Execution - Tạo/Mở rộng Tables trong NocoDB (TD_Games base)
- [ ] Mở rộng bảng **Users** (loại ns, giá cơ bản, stk ngân hàng...)
- [ ] Mở rộng bảng **Tasks** (trường Total Cost...)
- [ ] Tạo bảng **Task_Assignments** (phân công + chi phí từng người/task)
- [ ] Tạo bảng **Monthly_Payroll** (tổng hợp thanh toán cuối tháng)

## Execution - Tạo Views
- [ ] Tạo view "Monthly Summary" cho PM trên bảng Task_Assignments/Monthly_Payroll
- [ ] Tạo view "Unpaid Tasks" (chưa thanh toán)
- [ ] Tạo view "Member Payroll" (phân nhóm theo nhân sự)

## Verification
- [ ] Tạo records mẫu để test formula và linked relationships (Users -> Task_Assignments -> Tasks)
- [ ] Kiểm tra formula tính tổng cost
- [ ] Hướng dẫn thao tác chốt lương cuối tháng
