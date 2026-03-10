# PM Task Data Enhancements — Walkthrough

## Goal
Add new columns (Due Date, Closed Date, Bonus, Bonus Reason), inline Cost/Bonus editing, and additional filters (Assignee, Status, Due Date) to the PM Finance Tracking Task Data table.

## Changes Made

### NocoDB Schema
Added 4 columns to `PM_Tasks_Tracking`: `Due_Date` (text), `Closed_Date` (text), `Bonus` (decimal), `Bonus_Reason` (text).

---

### Backend — [pm-tracking.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/handlers/pm-tracking.js)
Added `Due_Date` and `Closed_Date` to taskData, converting ClickUp's Unix timestamps to ISO date strings.

### Backend — [nocodb.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/nocodb.js)
Updated `upsertPMTaskTracking` to include `Due_Date`/`Closed_Date` in both update and insert payloads.

### Backend — [api.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/api.js)
- **GET /pm-tracking**: Added `assignee` (like), `status` (eq), `hasDueDate` (yes/no) query filters.
- **PUT /pm-tracking/:id**: Added `Bonus`, `Bonus_Reason` to allowed update fields.
- **POST /pm-tracking/refresh**: Added `Due_Date`, `Closed_Date` to refreshed task data.

---

### Frontend — [index.html](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/index.html)
- Toolbar: Added 3 new filter selects — Assignees, Statuses, Due Date
- Table: Added 4 new columns — Due Date, Closed Date, Bonus, Bonus Reason

### Frontend — [app.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/app.js)
- `loadPMTracking()`: Renders all new columns, sends new filter params
- `populatePMFilters()`: Auto-populates Assignee, Status, Job Type dropdowns from data
- `inlineEditCost()`: Click a Cost cell → inline number input → Enter to save
- `inlineEditBonus()`: Click a Bonus cell → inline input → prompts for reason on save
- Edit modal: Added Bonus + Bonus Reason form fields

## Verification

### Full table with new columns and 6 filters
![PM Tracking with new columns and filters](file:///C:/Users/dangt/.gemini/antigravity/brain/498a5097-5772-44aa-8cbe-c02dec9cd185/pm_tracking_toolbar_and_table_1773158818938.png)

### Inline Cost editing verified ($0 → $100)
![Inline cost edit confirmation](file:///C:/Users/dangt/.gemini/antigravity/brain/498a5097-5772-44aa-8cbe-c02dec9cd185/pm_tracking_inline_edit_input_1773158842947.png)

### Browser recording
![PM Task Data enhancements demo](file:///C:/Users/dangt/.gemini/antigravity/brain/498a5097-5772-44aa-8cbe-c02dec9cd185/pm_task_data_verify_1773158783708.webp)

## Summary
| Feature | Status |
|---------|--------|
| Due Date & Closed Date columns | ✅ Synced from ClickUp |
| Cost inline edit (click to edit) | ✅ Working |
| Bonus + Bonus Reason columns | ✅ Working |
| Assignee filter | ✅ Dynamic from data |
| Status filter | ✅ Dynamic from data |
| Due Date filter | ✅ Has/No Due Date |
