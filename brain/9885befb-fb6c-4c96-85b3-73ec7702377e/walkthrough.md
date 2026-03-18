# Walkthrough — Session 2026-03-18 (Part 2)

## 1. CRM Activity Timeline ✅ (#6)

### Changes
- **[DB]** New table `crm_activities` (type, title, description, outcome, actor, date)
- **[NEW]** [ActivityTimeline.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/ActivityTimeline.tsx) — Per-client timeline with add form (📞/📧/🤝/📝), outcome tracking, delete
- **[MODIFY]** [crmService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/services/crmService.ts) — CRUD: `fetchActivities`, `createActivity`, `deleteActivity`
- **[MODIFY]** [ClientForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/ClientForm.tsx) — ActivityTimeline integrated below contacts
- **[MODIFY]** [CrmApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/CrmApp.tsx) — "Thống kê" tab → "Hoạt động" tab with `GlobalActivityFeed` + type filter

---

## 2. Role-Based Access + Employee Portal ✅ (#10)

### Role System

| Role | Tên | Apps |
|------|-----|------|
| `admin` | Giám đốc | Dashboard, Invoice, Expense, Workforce, CRM, HR, Chấm công, Tính lương |
| `ke_toan` | Kế toán | Invoice, Expense, Workforce, CRM, Tính lương |
| `hr` | HR | HR, Chấm công, Tính lương |
| `member` | Nhân viên | Employee Portal |

### Changes

**Core:**
- **[MODIFY]** [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) — `AccountUser.role` expanded: `admin | ke_toan | hr | member` + `employee_id`
- **[MODIFY]** [apps.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/config/apps.ts) — `roles[]` field per app, 9th app: Employee Portal
- **[MODIFY]** [HomeScreen.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/HomeScreen.tsx) — Filter apps by `currentUser.role`
- **[MODIFY]** [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx) — Portal route + `parseRole()` helper for all 4 roles

**Auth:**
- **[MODIFY]** [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/services/supabaseService.ts) — Email login support (username OR email), 4-role parsing, `employee_id` from metadata
- **[MODIFY]** [LoginScreen.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/LoginScreen.tsx) — Updated placeholder text
- **[DB]** Admin user → role `admin`, member user → role `ke_toan`

**Employee Portal:**
- **[NEW]** [PortalApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/portal/components/PortalApp.tsx) — 3 tabs: Thông tin công ty (employee grid), Bảng lương, Chấm công
- **[NEW]** [portalService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/portal/services/portalService.ts) — `fetchEmployeeDirectory()`, `fetchMyPayslips()`, `fetchMyAttendance()`

**Auto-Auth:**
- **[NEW]** Edge Function `create-employee-auth` — Auto-creates Supabase Auth account when HR adds a fulltime/parttime employee
- **[MODIFY]** [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts) — `saveEmployee()` calls Edge Function to create auth account

### Verification
- ✅ `tsc --noEmit` — 0 errors
- ✅ `vite build` — passes
