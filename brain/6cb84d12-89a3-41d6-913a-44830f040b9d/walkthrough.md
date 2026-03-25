# Walkthrough: Freelancer Form Redesign

## Thay đổi

File sửa: [EmployeeForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeForm.tsx)

### 1. Tách biệt 3 loại nhân sự
- **Freelancer**: form gọn ~15 fields, tập trung vào thông tin cần cho HĐKV
- **Parttime**: tách khỏi freelancer, có phòng ban + salary structure (giống fulltime)
- **Fulltime**: giữ nguyên

### 2. Freelancer — Fields đã lược bỏ
- ❌ Upload ảnh (avatar, CCCD trước/sau)
- ❌ Quốc tịch, địa chỉ tạm trú
- ❌ Phòng ban, cấp bậc, ngày bắt đầu, thử việc
- ❌ Số sổ bảo hiểm
- ❌ Cấu trúc lương, người phụ thuộc
- ❌ Múi giờ, phương thức thanh toán

### 3. Freelancer — Fields giữ lại
- ✅ Họ tên, email, SĐT, ngày sinh, giới tính, địa chỉ thường trú
- ✅ CCCD (số, ngày cấp, nơi cấp) — text only
- ✅ Email công việc (**tuỳ chọn** cho freelancer core)
- ✅ Chức danh, Portfolio URL, Mã số thuế
- ✅ Rate type/amount/currency, Chuyên môn
- ✅ Ngân hàng, Ghi chú & Tags

### 4. Validation
- Freelancer required: họ tên, email, SĐT, ngày sinh, giới tính, địa chỉ, CCCD + ngày/nơi cấp
- Fulltime/Parttime required: thêm work_email, temp_address, department, position, start_date

## Kết quả kiểm tra

![Form Freelancer đã redesign](C:/Users/dangt/.gemini/antigravity/brain/6cb84d12-89a3-41d6-913a-44830f040b9d/.system_generated/click_feedback/click_feedback_1774439484776.png)

- ✅ Freelancer form gọn, không có section fulltime/salary/dependents/photo upload
- ✅ Work email hiện "(tuỳ chọn)" cho freelancer
- ✅ Parttime có section riêng "🏢 Thông tin Part-time" + salary structure
- ✅ Fulltime giữ nguyên

![Recording](C:/Users/dangt/.gemini/antigravity/brain/6cb84d12-89a3-41d6-913a-44830f040b9d/verify_freelancer_form_1774439310310.webp)
