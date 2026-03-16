# HR App Verification Plan

- [x] Navigate to `http://localhost:3000/#hr/activity`
- [x] Verify department cards visibility
- [x] Check console for errors
- [x] Capture screenshot
- [x] Report findings

## Findings
- Navigated to HR app. The Departments tab is at `http://localhost:3000/#hr/departments`.
- **Only "Test Dept" card is visible.**
- Seeded departments (Art, Animation, VFX, R&D, Production, Management, HR, Finance) are **NOT showing** in the UI.
- Browser console shows NO relevant errors or failed network requests related to Supabase fetching.
- Screenshot `hr_departments_only_test_1773658938415.png` confirms the state.
