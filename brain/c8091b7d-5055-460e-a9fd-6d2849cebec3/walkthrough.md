# CRM Enhancements — Walkthrough

## Changes Made

### Database (Supabase)
- Added `lead_source`, `lead_direction`, `lead_source_detail` columns to `crm_clients`
- Created `crm_documents` table (contracts, NDA, invoices with file URLs)
- Created `crm_projects` table (projects with budget, dates, status)
- Created `crm_project_files` table (attachments/links per project)

### New CRM Tabs (5 total)

````carousel
![Khách hàng tab](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/crm_khach_hang_tab_1773586698418.png)
<!-- slide -->
![Dự án tab](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/crm_du_an_tab_1773586702915.png)
<!-- slide -->
![Tài liệu tab](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/crm_tai_lieu_tab_1773586713132.png)
<!-- slide -->
![Thanh toán tab — synced from Invoice app](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/crm_thanh_toan_tab_1773586722577.png)
<!-- slide -->
![Thống kê tab — lead source & direction stats](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/crm_thong_ke_tab_1773586730738.png)
````

### Files Modified/Created

| File | Action |
|------|--------|
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) | Added `CrmDocument`, `CrmProject`, `CrmProjectFile` + lead fields to `CrmClient` |
| [crmService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/services/crmService.ts) | Full CRUD for documents, projects, project_files + invoice sync |
| [ClientForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/ClientForm.tsx) | Added lead source section |
| [ProjectList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/ProjectList.tsx) | **NEW** — Project management with files |
| [DocumentList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/DocumentList.tsx) | **NEW** — Document management |
| [PaymentTracker.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/PaymentTracker.tsx) | **NEW** — Invoice sync from Invoice app |
| [CrmApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/CrmApp.tsx) | Expanded to 5 tabs + lead source stats |
| [useCrmState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/hooks/useCrmState.ts) | Updated tab type |

## Verification
- ✅ TypeScript compiles clean (`npx tsc --noEmit` — no errors)
- ✅ All 5 tabs render correctly
- ✅ Payment tab syncs invoices from `invoice_invoices` table
- ✅ Stats tab shows lead source & direction breakdowns
