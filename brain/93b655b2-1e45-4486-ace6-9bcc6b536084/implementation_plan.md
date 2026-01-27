# Plan: Enhance Form for Recruitment Industry

## Summary
Update the application form to be more suitable for a recruitment company with HR-specific fields.

## Proposed Changes

### Constants to Add/Update

#### [MODIFY] [ApplicationForm.tsx](file:///e:/TDC_App/TD_Consulting_App/hiring_tdconsulting/src/components/ApplicationForm.tsx)

**SOFTWARE_OPTIONS** - Update for recruitment:
```javascript
const SOFTWARE_OPTIONS = [
  "Microsoft Office", "LinkedIn Recruiter", "Slack", "Trello", "Notion",
  "Misa", "Jira", "GitHub", "HubSpot", "Pipedrive", "Canva", "Figma"
];
```

**Add SKILLS_OPTIONS** (new):
```javascript
const SKILLS_OPTIONS = [
  "Kỹ năng phỏng vấn", "Tìm kiếm ứng viên (Sourcing)", "Đàm phán lương",
  "Quản lý quan hệ khách hàng (CRM)", "Chạy Ads tuyển dụng"
];
```

**Add EXPERTISE_OPTIONS** (new):
```javascript
const EXPERTISE_OPTIONS = [
  "IT Recruitment", "Mass Recruitment", "Headhunting", "C&B",
  "General Accountant", "Tax Accountant", "Business Development", "Marketing"
];
```

**Add LANGUAGES** (new):
```javascript
const LANGUAGES = ["Tiếng Anh", "Tiếng Nhật", "Tiếng Trung", "Tiếng Hàn"];
const LANGUAGE_LEVELS = ["Cơ bản", "Trung cấp", "Thành thạo", "Bản ngữ"];
```

**Add SALARY_TYPES** (new):
```javascript
const SALARY_TYPES = ["Gross", "Net", "Lương cứng + Hoa hồng"];
```

---

### Schema Updates
- Change `portfolioUrl` → `linkedinUrl`
- Add `expertise`, `languages`, `salaryType` fields

---

### Form UI Updates
- Change "Portfolio URL" label → "LinkedIn Profile URL"
- Add "Chuyên môn chính" dropdown
- Add "Ngôn ngữ" section with checkboxes + proficiency
- Add Gross/Net/Commission option for salary
- Update placeholders for Vietnamese context

## Verification
Refresh http://localhost:8080 and test the form.
