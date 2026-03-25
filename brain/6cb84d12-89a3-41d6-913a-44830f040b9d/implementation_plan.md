# Freelancer Form Redesign — Tách biệt Freelancer khỏi Fulltime/Parttime

## Mục tiêu
Thiết kế lại form tạo nhân sự Freelancer để gọn hơn, chỉ giữ các field cần thiết cho lưu trữ hồ sơ + làm hợp đồng khoán việc (HĐKV). Đồng thời tách biệt rõ ràng section UI giữa **Freelancer** và **Parttime**.

---

## Proposed Changes

### EmployeeForm Component

#### [MODIFY] [EmployeeForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeForm.tsx)

**1. Tách section Freelancer và Parttime**
- Hiện tại dòng 761: `(form.type === 'freelancer' || form.type === 'parttime')` → dùng chung 1 section "Thông tin Freelancer"
- **Sửa**: Freelancer có section riêng, Parttime có section riêng (parttime giữ nguyên như cũ, gần giống fulltime hơn)

**2. Redesign form khi `type === 'freelancer'`**

Form Freelancer sẽ gồm các section sau:

**Section 1: Thông tin cơ bản** (giữ nguyên nhưng bỏ bớt)
- ✅ `full_name` (required)
- ✅ `type` selector (required)
- ✅ `status` selector
- ✅ `email` cá nhân (required — dùng cho hợp đồng)
- ✅ `work_email` (**optional** — cho freelancer core)
- ✅ `phone` (required — dùng cho hợp đồng)
- ✅ `date_of_birth` (required — dùng cho hợp đồng)
- ✅ `gender` (required — dùng cho hợp đồng)
- ❌ Bỏ `nationality`
- ✅ `address` thường trú (required — dùng cho hợp đồng)
- ❌ Bỏ `temp_address` tạm trú

**Section 2: CCCD** (giữ fields, bỏ upload ảnh)
- ✅ `id_number` (required — dùng cho hợp đồng)
- ✅ `id_issue_date` (required — dùng cho hợp đồng)
- ✅ `id_issue_place` (required — dùng cho hợp đồng)
- ❌ Bỏ `avatar_url` upload ảnh đại diện
- ❌ Bỏ `id_card_front_url` upload CCCD mặt trước
- ❌ Bỏ `id_card_back_url` upload CCCD mặt sau

**Section 3: Thông tin Freelancer** (giữ)
- ✅ `portfolio_url`
- ✅ `position` (chức danh)
- ✅ `specializations` (chuyên môn)
- ✅ `rate_type`, `rate_amount`, `rate_currency`
- ❌ Bỏ `timezone`
- ❌ Bỏ `payment_method`

**Section 4: Ngân hàng & Thuế** (gộp)
- ✅ `bank_name`, `bank_account`, `bank_branch`
- ✅ `tax_code` (để kê khai thuế TNCN)

**Section 5: Ghi chú & Tags** (giữ nguyên)
- ✅ `notes`, `tags`

**Bỏ hoàn toàn cho Freelancer:**
- ❌ Section "Thông tin Fulltime" (department, level, start_date, probation_end)
- ❌ Section "Cấu trúc lương" (salary components)
- ❌ Section "Người phụ thuộc"
- ❌ `insurance_number`, `salary`, `salary_currency`

**3. Cập nhật required fields validation**

Dòng 71-88: thêm case riêng cho `freelancer`:
```tsx
const requiredFields = [
  { key: 'full_name', label: 'Họ tên' },
  { key: 'email', label: 'Email cá nhân' },
  { key: 'phone', label: 'SĐT' },
  { key: 'date_of_birth', label: 'Ngày sinh' },
  { key: 'gender', label: 'Giới tính' },
  { key: 'address', label: 'Địa chỉ thường trú' },
  { key: 'id_number', label: 'CMND/CCCD' },
  ...(form.type === 'fulltime' ? [
    // fulltime-specific required fields  
    { key: 'work_email', label: 'Email công việc' },
    { key: 'temp_address', label: 'Địa chỉ tạm trú' },
    { key: 'id_issue_date', label: 'Ngày cấp CMND' },
    { key: 'id_issue_place', label: 'Nơi cấp' },
    { key: 'department_id', label: 'Phòng ban' },
    { key: 'position', label: 'Chức danh' },
    { key: 'start_date', label: 'Ngày bắt đầu' },
  ] : form.type === 'freelancer' ? [
    // freelancer: CCCD info required for contract
    { key: 'id_issue_date', label: 'Ngày cấp CMND' },
    { key: 'id_issue_place', label: 'Nơi cấp' },
  ] : [
    // parttime: similar to fulltime  
    { key: 'work_email', label: 'Email công việc' },
    { key: 'temp_address', label: 'Địa chỉ tạm trú' },
    { key: 'id_issue_date', label: 'Ngày cấp CMND' },
    { key: 'id_issue_place', label: 'Nơi cấp' },
    { key: 'department_id', label: 'Phòng ban' },
    { key: 'position', label: 'Chức danh' },
    { key: 'start_date', label: 'Ngày bắt đầu' },
  ]),
];
```

**4. Conditional section rendering**

Thay đổi logic hiển thị section:
- Section "Thông tin cơ bản": hiện cho cả 3 type, nhưng hide `temp_address` và `nationality` khi `type === 'freelancer'`
- Section "CCCD & Photos": Freelancer chỉ hiện 3 fields CCCD (số, ngày cấp, nơi cấp), bỏ upload ảnh
- Section "Fulltime": chỉ hiện khi `type === 'fulltime'` (hiện tại đúng rồi)
- Section "Cấu trúc lương": chỉ hiện khi `type === 'fulltime'` (hiện tại đúng rồi)  
- Section "Người phụ thuộc": chỉ hiện khi `type === 'fulltime'` (hiện tại đúng rồi)
- Section "Freelancer": chỉ hiện khi `type === 'freelancer'` (TÁCH khỏi parttime)
- Section "Parttime": mới thêm, hiện khi `type === 'parttime'` — giống fulltime nhưng không cần salary structure, không cần người phụ thuộc (hoặc giữ section freelancer cũ cho parttime)
- Section "Ngân hàng": hiện cho cả 3 type, freelancer thêm field `tax_code`
- Section "Ghi chú & Tags": hiện cho cả 3 type

---

## Verification Plan

### Browser Testing
1. Mở app tại `http://localhost:3000/#hr/employeeForm`
2. Chọn type **Freelancer** → kiểm tra các section hiển thị đúng (không có dept, salary structure, người phụ thuộc, upload ảnh)
3. Chọn type **Fulltime** → kiểm tra các section đầy đủ như cũ
4. Chọn type **Parttime** → kiểm tra có section riêng
5. Thử submit Freelancer form với các field required bị trống → kiểm tra validation
6. Điền đầy đủ → submit → kiểm tra tạo thành công
