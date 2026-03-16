# HR Management App — Walkthrough

## What Was Built

### Database (Supabase — `fifuhkupaqcfjwyouwpa`)
8 tables with RLS + auto-trigger for employee codes + 8 seeded departments:
`hr_employees`, `hr_departments`, `hr_contracts`, `hr_position_history`, `hr_evaluations`, `hr_project_history`, `hr_documents`, `hr_reminders`

### Frontend Components

| Component | Purpose |
|-----------|---------|
| [HrApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/HrApp.tsx) | Main shell (3 tabs) |
| [EmployeeList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeList.tsx) | Search/filter/summary cards |
| [EmployeeForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeForm.tsx) | Conditional fulltime/freelancer form |
| [EmployeeDetail.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeDetail.tsx) | Detail view (5 tabs) |
| [DepartmentManager.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/DepartmentManager.tsx) | CRUD departments |
| [ReminderDashboard.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/ReminderDashboard.tsx) | Auto-scan reminders |
| [DocumentManager.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/DocumentManager.tsx) | R2 file upload + preview |
| [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts) | Supabase CRUD + R2 upload |

---

## Bug Fixes
- **PGRST201 Ambiguous FK**: Fixed by explicit hint `!hr_employees_department_id_fkey`
- **Promise.all → Promise.allSettled**: One failed fetch no longer kills all parallel loads

## Phase 7: Cloudflare R2 Upload
- Reuses existing `r2-expense-upload` Edge Function (same as CRM)
- `uploadFileToR2()` + `toPublicUrl()` added to `hrService.ts`
- `DocumentManager.tsx` with drag-drop, live preview (images/PDF), download, inline delete
- 7 document categories: Hợp đồng, CMND/CCCD, Bằng cấp, Bảo hiểm, Thuế, Portfolio, Khác

## Phase 8: Data Migration
Migrated 3 freelancers from `wf_workers` → `hr_employees`:

| Code | Name | Email |
|------|------|-------|
| FL-001 | Nguyễn Ngọc Anh | 93ngocnguyen@gmail.com |
| FL-002 | Nguyễn Quang Huy | nqhuy17@gmail.com |
| FL-003 | Lê Văn Khiêm | khiemlv.tdconsulting@gmail.com |

---

## Verification Screenshots

### Employees — 3 migrated freelancers
![Migrated employees](C:/Users/dangt/.gemini/antigravity/brain/33b1daf7-1d06-454f-860b-4f168b4d09f3/hr_employees_migrated.png)

### Departments — 9 departments loaded
![Departments](C:/Users/dangt/.gemini/antigravity/brain/33b1daf7-1d06-454f-860b-4f168b4d09f3/hr_phongban.png)

### Document Manager — Upload form
![Document Manager](C:/Users/dangt/.gemini/antigravity/brain/33b1daf7-1d06-454f-860b-4f168b4d09f3/hr_docmanager.png)

### Full Flow Recording
![HR migration and document upload verification](C:/Users/dangt/.gemini/antigravity/brain/33b1daf7-1d06-454f-860b-4f168b4d09f3/hr_migration_verify_1773659766984.webp)
