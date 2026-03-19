# Employee Onboarding Flow

Triển khai luồng onboarding nhân viên mới: HR nhập thông tin cơ bản → gửi link đăng nhập → nhân viên đổi password → nhân viên tự điền hồ sơ.

## Hiện trạng (đã có sẵn)

Hệ thống **đã có sẵn** các phần sau:
- ✅ `saveEmployee()` trong `hrService.ts` tự động gọi `create-employee-auth` Edge Function để invite nhân viên qua email công việc
- ✅ `SetPasswordScreen.tsx` xử lý đổi password lần đầu
- ✅ `App.tsx` phát hiện invite flow → hiển thị SetPasswordScreen → chuyển member role tới Portal
- ✅ `PortalApp.tsx` với 4 tab: Thông tin công ty / Bảng lương / Chấm công / Nghỉ phép

## Proposed Changes

### HR Module — Quick Add Employee

#### [NEW] [QuickAddEmployee.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/QuickAddEmployee.tsx)

Form đơn giản chỉ chứa các trường HR cần nhập khi onboarding:
- **Tên** (`full_name`)
- **Email công việc** (`work_email`)
- **Phòng ban** (`department_id`)
- **Chức danh** (`position`)
- **Cấp bậc** (`level`)
- **Ngày bắt đầu** (`start_date`) → auto-tính `probation_end` (+2 tháng)
- **Cấu trúc lương** (salary components)

Khi submit → gọi `saveEmployee()` (auto-invite) → hiển thị toast "Đã thêm NV & gửi email mời".

---

#### [MODIFY] [HrApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/HrApp.tsx)

Thêm tab `quickAdd` vào router, map tới `QuickAddEmployee` component.

#### [MODIFY] [EmployeeList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeList.tsx)

Thêm nút "⚡ Thêm nhanh" bên cạnh nút "Thêm nhân sự" hiện tại.

---

### Portal Module — Profile Tab

#### [NEW] [ProfileTab.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/portal/components/ProfileTab.tsx)

Tab "Hồ sơ của tôi" cho nhân viên xem/chỉnh sửa thông tin cá nhân:

**Trường READ-ONLY** (HR/Admin điền, nhân viên không chỉnh được):
| Trường | Lý do |
|---|---|
| `work_email` | Email công ty, do IT/HR cấp |
| `department_id` | Phòng ban, do HR chỉ định |
| `position` | Chức danh, do HR chỉ định |
| `level` | Cấp bậc, do HR chỉ định |
| `start_date` | Ngày bắt đầu, do HR ghi nhận |
| `probation_end` | Hết thử việc, do HR ghi nhận |
| `salary` / salary components | Lương, do Kế toán/HR quản lý |
| `type` | Loại nhân sự (FT/FL/PT) |
| `status` | Trạng thái (active/inactive) |
| `employee_code` | Mã nhân viên, tự sinh |

**Trường EDITABLE** (nhân viên tự điền/chỉnh):
| Trường | Mô tả |
|---|---|
| `full_name` | Họ tên |
| `email` | Email cá nhân |
| `phone` | SĐT |
| `date_of_birth` | Ngày sinh |
| `gender` | Giới tính |
| `nationality` | Quốc tịch |
| `address` | Địa chỉ thường trú |
| `temp_address` | Địa chỉ tạm trú |
| `id_number` | CMND/CCCD |
| `id_issue_date` | Ngày cấp |
| `id_issue_place` | Nơi cấp |
| `avatar_url` | Ảnh đại diện |
| `id_card_front_url` | CCCD mặt trước |
| `id_card_back_url` | CCCD mặt sau |
| `tax_code` | MST cá nhân |
| `insurance_number` | Số sổ bảo hiểm |
| `bank_name` | Tên NH |
| `bank_account` | STK |
| `bank_branch` | Chi nhánh |

Hiển thị **thanh tiến trình điền hồ sơ** (profile completion %) dựa trên số trường đã có dữ liệu.

---

#### [MODIFY] [portalService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/portal/services/portalService.ts)

Thêm 2 hàm:
- `fetchMyProfile(employeeId)` — lấy full thông tin nhân viên
- `updateMyProfile(employeeId, updates)` — cập nhật các trường editable

#### [MODIFY] [PortalApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/portal/components/PortalApp.tsx)

Thêm tab **"Hồ sơ"** vào navbar, map tới `ProfileTab`. Đặt làm tab mặc đầu tiên khi profile chưa hoàn chỉnh.

---

### App.tsx — Profile Completion Check

#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)

Sau khi SetPasswordScreen `onComplete`:
- Nếu role === `member` → navigate tới `portal` (đã có)
- Portal sẽ tự phát hiện profile chưa hoàn chỉnh → chuyển sang tab Hồ sơ

## Verification Plan

### Browser Testing
1. Mở app HR → click "⚡ Thêm nhanh" → điền thông tin tối thiểu → Submit
2. Kiểm tra toast thành công + nhân viên xuất hiện trong danh sách
3. Đăng nhập bằng account nhân viên mới → phải qua SetPasswordScreen
4. Sau đổi password → chuyển tới Portal → tab Hồ sơ hiển thị
5. Kiểm tra các trường HR-set hiển thị read-only (không editable)
6. Kiểm tra các trường cá nhân có thể chỉnh sửa và lưu thành công
7. Kiểm tra profile completion % cập nhật đúng
