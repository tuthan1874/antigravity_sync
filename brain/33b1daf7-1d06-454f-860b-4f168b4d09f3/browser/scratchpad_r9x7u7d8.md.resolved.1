# HR App Investigation Scratchpad

## Current Status
- Navigated to `http://localhost:3000/#hr/departments`.
- Hard reload performed.
- UI shows **zero** department cards, despite 9 departments existing in the database (verified via network response).
- Error toast observed: "Could not embed because more than one relationship was found for 'hr_employees' and 'hr_departments'".

## Findings
- **API Request 344 (GET `hr_employees`) failed with 300 (Multiple Choices)**.
  - Reason: PostgREST PGRST201. Ambiguous relationship between `hr_employees` and `hr_departments`.
  - Multiple FKs: `hr_employees.department_id` and `hr_departments.manager_id`.
  - Response Body: `{"code":"PGRST201","message":"Could not embed because more than one relationship was found for 'hr_employees' and 'hr_departments'", ...}`
- **API Request 345 (GET `hr_departments`) succeeded with 200**.
  - Returned 9 departments (Animation, Art, Finance, HR, Management, Production, R&D, Test Dept, VFX).
- **UI Issue**: The departments are not rendered because the `loadAll` function in `useHrState.ts` likely uses `Promise.all`. Since the employee fetch fails, the entire initialization promise rejects, leaving the state empty.
- **Other Tabs**: 
  - "Nhân sự" (Personnel) is empty due to the same failed request.
  - "Nhắc việc" (Reminders) shows "No reminders" which is technically correct (request 346 returned `[]`).

## Recommendation (Fix)
In `hrService.ts`, the `fetchEmployees` query must be updated to specify the foreign key:
```typescript
.select('*, department:hr_departments!hr_employees_department_id_fkey(*)')
```
This disambiguates which relationship to use for embedding.
