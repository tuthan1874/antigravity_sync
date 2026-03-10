# Decouple PM Tracking — Independent Config

## Task 1: Create NocoDB Table
- [ ] Create `PM_Tracking_Configs` table with columns: Title, ClickUp_Type, ClickUp_ID, Job_Type, Enabled
- [ ] Migrate existing KABAM data (List_ID=901815849460, Job_Type=Art)

## Task 2: Backend — NocoDB Functions
- [ ] Add CRUD functions in `nocodb.js` for PM_Tracking_Configs
- [ ] Add `findPMTrackingConfig(taskDeet)` matching logic (list→folder→space)

## Task 3: Backend — Handler + API
- [ ] Rewrite `pm-tracking.js` to use new config table
- [ ] Add CRUD routes in `api.js` for `/api/pm-tracking-configs`

## Task 4: Frontend UI
- [ ] Add PM Tracking Configs section to `index.html` (table + add button)
- [ ] Add `loadPMTrackingConfigs()`, modal, toggle in `app.js`

## Task 5: Verification + Commit
- [ ] Test in browser
- [ ] Commit + push
