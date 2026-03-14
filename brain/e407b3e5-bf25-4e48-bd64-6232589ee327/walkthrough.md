# Headhunter Landing Page — Walkthrough

## Overview

Built a personal Headhunter landing page for **Linh Nguyễn** with soft pink theme, glassmorphism UI, job listings, application form, Google Sheets integration, and a dedicated profile page.

---

## Files Created

| File | Purpose |
|------|---------|
| [index.html](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/index.html) | Main landing page |
| [profile.html](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/profile.html) | Headhunter profile page |
| [css/styles.css](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/css/styles.css) | Complete design system |
| [js/app.js](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/js/app.js) | Navbar, mobile menu, scroll effects |
| [js/jobs.js](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/js/jobs.js) | 12 demo jobs, filtering, rendering |
| [js/form.js](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/js/form.js) | Form validation & Google Sheets submission |
| [Code.gs](file:///e:/TDC_App/TDGAMES_App/LandingPage_Headhunt/google-apps-script/Code.gs) | Google Apps Script backend |

---

## Screenshots

### Landing Page

````carousel
![Hero Section — Personalized branding with CTA](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/hero_section_1773497685977.png)
<!-- slide -->
![Job Listings — 12 demo jobs with category filters](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/job_listings_section_1773497688313.png)
<!-- slide -->
![About Section — Intro & key benefits](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/about_section_1773497694266.png)
<!-- slide -->
![Apply Modal — Full application form](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/apply_modal_1773497723629.png)
<!-- slide -->
![Footer — Contact, social links, newsletter](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/footer_section_1773497733299.png)
````

### Profile Page

````carousel
![Profile Header — Bio, stats, expertise areas](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/profile_header_stats_1773497797429.png)
<!-- slide -->
![Experience & Testimonials — Timeline and client reviews](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/profile_experience_testimonials_1773497811477.png)
````

### Full Page Recording

![Landing page walkthrough recording](C:/Users/dangt/.gemini/antigravity/brain/e407b3e5-bf25-4e48-bd64-6232589ee327/verify_landing_page_1773497596240.webp)

---

## What's Working

- ✅ Soft pink theme with glassmorphism cards
- ✅ Responsive design (mobile/tablet/desktop)
- ✅ 12 demo job listings with category filtering (IT, Finance, Marketing, Management)
- ✅ Job application modal with full form validation
- ✅ Demo mode for form submission (shows success toast)
- ✅ Profile page with bio, stats, expertise, experience timeline, testimonials
- ✅ Sticky navbar with scroll effects
- ✅ Scroll-to-top button
- ✅ Scroll-reveal animations
- ✅ Mobile hamburger menu

---

## Next Steps (User Action Required)

> [!IMPORTANT]
> To enable real form submissions to Google Sheets + email notifications:

1. **Deploy Google Apps Script:**
   - Open [Google Apps Script](https://script.google.com), paste contents of `google-apps-script/Code.gs`
   - Update `EMAIL_RECIPIENT` with your email address
   - Deploy as Web App → set access to "Anyone"
   - Copy the deployed URL

2. **Update `js/form.js`:**
   - Replace `'YOUR_GOOGLE_SCRIPT_URL_HERE'` with your deployed URL

3. **Update Content:**
   - Replace demo job data in `js/jobs.js`
   - Update profile info in `profile.html`
   - Replace placeholder avatar image
