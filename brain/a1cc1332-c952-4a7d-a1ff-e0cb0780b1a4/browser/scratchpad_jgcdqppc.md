# Task: Examine HR Contract PDF Templates

## Plan
- [x] Examine HĐLĐ (Labour Contract) PDF
    - [x] Open file
    - [x] Scroll and screenshot all pages
    - [x] List sections and data fields
- [x] Examine HĐTV (Probation Contract) PDF
    - [x] Open file
    - [x] Scroll and screenshot all pages
    - [x] List sections and data fields
- [x] Examine Cam kết bảo mật (Confidentiality Agreement) PDF
    - [x] Open file
    - [x] Scroll and screenshot all pages
    - [x] List sections and data fields
- [x] Consolidate findings and report back

## Findings
### 1. HĐLĐ (Labour Contract)
- **Total Pages:** 5
- **Structure:**
    - Header: Social Republic of Vietnam, INDEPENDENCE - FREEDOM - HAPPINESS
    - Title: HỢP ĐỒNG LAO ĐỘNG
    - Parties:
        - Party A: CÔNG TY TNHH TD GAMES (Representative: Đặng Thế Toàn - CEO)
        - Party B: Employee details
- **Fields (Page 1):**
    - Contract Number (Số)
    - Signed Date (Ngày, tháng, năm)
    - Employee Name (Họ và tên)
    - DOB (Ngày tháng năm sinh)
    - Nationality (Quốc tịch)
    - Gender (Giới tính)
    - Permanent Address (Địa chỉ thường trú)
    - ID Number (Số CMND)
    - ID Issue Date (Ngày cấp)
    - ID Issue Place (Nơi cấp)
    - Position (Vị trí - Section 1.3)
    - Base Salary (Mức lương cơ bản - Section 3.1)
    - Allowances (Phụ cấp - Section 5.1): Meal (Ăn trưa), Phone (Điện thoại), Petrol (Xăng xe), Uniform (Trang phục), KPI.

### 2. HĐTV (Probation Contract)
- **Total Pages:** 4
- **Structure:** Similar to HĐLĐ but focused on probation terms.
- **Fields:**
    - Contract Number (Số HĐTV)
    - Signed Date
    - Employee info (Same as HĐLĐ)
    - Start Date, End Date (Thời điểm bắt đầu/kết thúc - Section 1.3, 1.4)
    - Department (Bộ phận công tác - Section 1.6)
    - Position (Chức danh chuyên môn - Section 1.7)
    - Base Salary (Mức lương cơ bản - Section 3.1.1)
    - Probation Salary (Mức lương thử việc = 85% base - Section 3.1.1)
    - Allowances (Section 3.1.2): Meal, Phone, Petrol, Uniform, KPI.

### 3. Cam kết bảo mật (Confidentiality Agreement)
- **Total Pages:** 3
- **Structure:** 8 sections focused on confidentiality and non-compete.
- **Fields:**
    - Name (Tôi tên là)
    - DOB (Sinh ngày)
    - ID details: Number (Số CMND), Issue Date (Ngày cấp), Issue Place (Nơi cấp)
    - Permanent Address (Hộ khẩu thường trú)
    - Current Address (Chỗ ở hiện tại)
    - Working at Department (Đang làm việc tại)
    - Position (Chức danh)

## Summary of Data Fields to implement export:
Based on these templates, the following fields are required from the HR data:
1. **Personal info**: Name, DOB, Gender, Nationality.
2. **Identification**: ID Number, Issue Date, Issue Place.
3. **Contact info**: Permanent Address, Current Address.
4. **Job info**: Department, Position, Start Date, End Date (for probation).
5. **Salary info**: Base Salary, Probation Salary (85% of base), and specific allowances (Meal, Phone, Petrol, Uniform, KPI).
6. **Contract info**: Contract Number, Signed Date.
