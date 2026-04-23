# ✅ Sprint 1 — HR → Workforce Sync — HOÀN THÀNH

## Kết quả

![HR Employee List with Workforce Sync](C:/Users/dangt/.gemini/antigravity/brain/37d725e8-f76d-4cff-89bb-cec3b02421df/.system_generated/click_feedback/click_feedback_1776956097977.png)

## Checklist Sprint 1

| # | Task | Status |
|---|------|--------|
| 1 | Backfill: Sync 9 nhân viên hiện tại | ✅ Done |
| 2 | `hrService.ts`: Thêm `syncEmployeeToWorkforce()` | ✅ Done |
| 3 | Hook vào `saveEmployee()` + `updateEmployee()` | ✅ Done |
| 4 | Hook vào `QuickAddEmployee` flow | ✅ Auto-covered |
| 5 | UI: Nút "Sync WF" + badge "WF ✓" | ✅ Done |
| 6 | Test trên browser | ✅ Verified |

## Chi tiết thay đổi

### Database (Supabase SQL)
- Backfill: 9 HR employees → 9 wf_workers (đã link worker_id)
- Cleanup: Xóa 5 bản ghi wf_workers trùng lặp (empty email)
- Fixed: Mapping chính xác 4 fulltime (inhouse) + 5 freelancer

### Code Changes

| File | Changes |
|------|---------|
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) | Added `worker_id: string \| null` to `HrEmployee` |
| [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts) | Added `syncEmployeeToWorkforce()` + `syncAllEmployeesToWorkforce()`, hooked into save/update |
| [useHrState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/hooks/useHrState.ts) | Added `handleSyncAllToWorkforce` handler |
| [EmployeeList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeList.tsx) | Added "Sync WF" button + "WF ✓" badge per employee |
| [HrApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/HrApp.tsx) | Passed `onSyncWorkforce` prop |

### Luồng hoạt động

```mermaid
sequenceDiagram
    participant HR as HR Module
    participant SVC as hrService
    participant DB as Supabase
    participant WF as wf_workers

    HR->>SVC: saveEmployee(data)
    SVC->>DB: INSERT hr_employees
    DB-->>SVC: return saved employee
    SVC->>SVC: syncEmployeeToWorkforce(saved)
    alt Has worker_id
        SVC->>WF: UPDATE wf_workers
    else Find by email
        SVC->>WF: SELECT by email
        SVC->>WF: UPDATE + link
    else New
        SVC->>WF: INSERT new worker
        SVC->>DB: UPDATE hr_employees.worker_id
    end
    SVC-->>HR: return saved employee
```

## Next: Sprint 2
- Dashboard Service (`dashboardService.ts`)
- KPI calculation for fulltime employees
- Financial summary aggregation
