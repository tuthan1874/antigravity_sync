# Headhunter Landing Page

Landing page cá nhân cho Headhunter - nơi đăng tin tuyển dụng, ứng viên có thể apply job, dữ liệu gửi về Google Sheet và thông báo qua email. Có trang profile riêng giới thiệu Headhunter.

## User Review Required

> [!IMPORTANT]
> **Google Sheets & Email Integration**: Sử dụng **Google Apps Script** (miễn phí) làm backend xử lý form submissions. Bạn cần:
> 1. Tạo 1 Google Sheet mới
> 2. Deploy Google Apps Script (sẽ hướng dẫn chi tiết)
> 3. Cung cấp email nhận notification

> [!NOTE]
> **Thông tin cá nhân**: Cần bạn cung cấp thông tin profile Headhunter:
> - Tên, chức danh, ảnh đại diện
> - Mô tả bản thân / kinh nghiệm
> - Các lĩnh vực chuyên môn tuyển dụng
> - Thông tin liên hệ (email, LinkedIn, phone)
> - Danh sách job mẫu ban đầu (nếu có)

**Tạm thời sẽ dùng placeholder data, bạn có thể thay đổi sau.**

## Proposed Changes

### Project Structure

```
LandingPage_Headhunt/
├── index.html          # Trang chính - Job listings + Hero
├── profile.html        # Trang profile Headhunter
├── css/
│   └── styles.css      # Main stylesheet
├── js/
│   ├── app.js          # Main app logic
│   ├── jobs.js         # Job data & rendering
│   └── form.js         # Form submission & Google Sheets integration
├── assets/
│   └── images/         # Images, icons
└── google-apps-script/
    └── Code.gs         # Google Apps Script code (deploy riêng)
```

---

### 1. Landing Page (`index.html`)

#### Sections:
- **Navbar**: Logo, navigation links (Jobs, About, Profile, Contact)
- **Hero Section**: Banner giới thiệu headhunter với tagline, CTA "Xem việc làm"
- **Job Listings**: Grid/cards hiển thị các job mở, filter theo ngành/vị trí
- **About Brief**: Tóm tắt ngắn về headhunter, link đến trang Profile
- **Footer**: Contact info, social links

#### Design:
- Dark theme premium với accent color (gold/amber)
- Glassmorphism cards cho job listings
- Smooth scroll animations
- Responsive cho mobile/tablet/desktop

---

### 2. Profile Page (`profile.html`)

#### Sections:
- **Hero Banner**: Ảnh cover + avatar + tên + chức danh
- **About Me**: Giới thiệu chi tiết
- **Expertise**: Các lĩnh vực chuyên môn (cards/badges)
- **Stats**: Số năm kinh nghiệm, số ứng viên đã giới thiệu, tỷ lệ thành công
- **Testimonials**: Review từ clients/candidates
- **Contact Form**: Form liên hệ trực tiếp

---

### 3. Job Application Modal

- Modal popup khi click "Apply" trên mỗi job card
- Fields: Họ tên, Email, Phone, LinkedIn, Position applying, CV upload link (Google Drive), Cover letter
- Submit → Google Apps Script → Google Sheet + Email notification

---

### 4. Google Apps Script Backend

#### [NEW] `google-apps-script/Code.gs`

Script xử lý:
1. **Nhận POST request** từ form application
2. **Ghi dữ liệu** vào Google Sheet (tự tạo sheet nếu chưa có)
3. **Gửi email notification** đến headhunter
4. **Return JSON response** cho frontend

Columns trong Google Sheet:
| Timestamp | Job Title | Full Name | Email | Phone | LinkedIn | CV Link | Cover Letter | Status |

---

### 5. CSS Design System (`css/styles.css`)

- CSS Variables cho color palette (dark theme)
- Typography: Google Fonts (Inter/Outfit)
- Components: Cards, Buttons, Modals, Forms, Badges
- Animations: Fade-in, slide-up, hover effects
- Responsive breakpoints: mobile (< 768px), tablet (768-1024px), desktop (> 1024px)

---

### 6. JavaScript Modules

#### [NEW] `js/app.js`
- Navigation, smooth scroll, mobile menu toggle
- Page initialization

#### [NEW] `js/jobs.js`
- Job data (JSON array - dễ dàng cập nhật)
- Job card rendering
- Filter/search functionality
- Job detail modal

#### [NEW] `js/form.js`
- Form validation
- Submit to Google Apps Script
- Success/error handling
- Loading states

## Verification Plan

### Browser Testing
1. Mở `index.html` trong browser, kiểm tra tất cả sections render đúng
2. Click các job cards, verify modal hiện lên
3. Test form validation (submit form trống, email sai format)
4. Test responsive bằng cách resize browser
5. Navigate đến `profile.html`, verify trang render đúng
6. Test navigation links giữa 2 trang

### Manual Verification (cần user)
1. Deploy Google Apps Script và test form submission thực tế
2. Verify data xuất hiện trong Google Sheet
3. Verify email notification được gửi
4. User review overall design và content
