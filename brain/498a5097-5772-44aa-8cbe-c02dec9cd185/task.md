# List Configs Pause/Active + PM Tracking Fix

## Task 1: Add `Enabled` and `Job_Type` columns to NocoDB ListMappings
- [x] Add `Enabled` column (SingleLineText) to ListMappings table
- [x] Add `Job_Type` column (SingleLineText) to ListMappings table  
- [x] Update existing record (Id=2, KABAM/ORCA) with `Job_Type=Art`, `Enabled=Active`

## Task 2: Add Pause/Active UI to List Configs
- [x] Update `index.html` — add Job Type + Status columns to table header
- [x] Update `app.js` — `loadListMappings()` to show Job Type, Enabled badge + toggle button
- [x] Update `app.js` — `openModal('list-mapping')` to include Enabled and Job_Type fields
- [x] Add `toggleListMappingStatus()` function for quick pause/active toggle

## Task 3: Fix PM Tracking (Backend)
- [x] Update `pm-tracking.js` handler to check `listMapping.Enabled` before processing
- [x] Update `slack-automation.js` to check `listMapping.Enabled` before processing  
- [x] Update `discord-automation.js` to check `listMapping.Enabled` before processing

## Task 4: Verification
- [x] Start dev server and test List Configs page — ✅ columns, toggle, modal all working
- [x] Verify PM Tracking page still displays existing data — ✅ Art + Animation tasks loaded
