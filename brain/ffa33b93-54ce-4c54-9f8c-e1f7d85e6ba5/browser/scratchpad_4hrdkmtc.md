# UI/UX Audit Plan

## Tasks:
- [x] Visit `http://localhost:3000` (Landing Page) & Take Screenshot
- [x] Visit `http://localhost:3000/login` & Take Screenshot
- [x] Visit `http://localhost:3000/signup` & Take Screenshot
- [x] Visit `http://localhost:3000/dashboard` & Take Screenshot
- [ ] Review `Style_Guild.md` for design principles
- [x] Document all visual issues (layout, alignment, spacing, etc.)

## Findings:

### General Issues:
- Inconsistent input styling across auth pages.
- Large, distracting glow effects on primary buttons.
- Excessive whitespace and disconnected layouts in the dashboard.
- High contrast between dark backgrounds and light gray input backgrounds on auth pages.

### Landing Page:
- "Log in" and "Get Started" buttons in the navbar are too close to the screen edge.
- Minimal footer with very little information or links.
- Feature icons are relatively small compared to their containers.

### Auth Pages (Login/Signup):
- Signup page: "Full Name" input has a transparent/dark background (only border visible), while "Email" and "Password" have solid light gray backgrounds.
- Card backgrounds are extremely dark, almost blending into the page background.
- "Sign up" / "Sign in" links at the bottom are orange but lack a standard link feel (e.g., hover effect or underline).

### Dashboard:
- Sidebar: "Projects" item is active but the sidebar itself is very narrow and minimalist.
- Header: Massive "Projects" background text is too prominent and distracting.
- Hero section for empty state is disconnected from the "Your Projects" title.
- Header elements (user profile, etc.) are small compared to the huge background text.
- Spacing between the top header and content area is inconsistent.
