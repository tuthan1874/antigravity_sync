# PM Tracking — Independent Config + List Configs Fix

## Session 1: List Configs Pause/Active + PM Tracking Fix

### Changes
- Added `Job_Type` and `Enabled` columns to `ListMappings` NocoDB table
- Added ⏸️/▶️ toggle to List Configs UI
- Fixed PM Tracking root cause: missing `Job_Type` column → handler was skipping all tasks

---

## Session 2: Decouple PM Tracking from List Configs

### Problem
PM Tracking was tied to `ListMappings` — could only track by List ID and only if a List Config existed.

### Solution
Created independent `PM_Tracking_Configs` table supporting 3 tracking levels:

| Level | Use Case |
|-------|----------|
| 🌐 **Space** | Track ALL tasks across all folders/lists in a space |
| 📁 **Folder** | Track all tasks within a specific folder |
| 📋 **List** | Track tasks in a specific list (most specific) |

### Matching Priority
When a webhook arrives: **List match → Folder match → Space match** (most specific wins)

### Files Changed
- **`nocodb.js`** — CRUD + `findPMTrackingConfig()` with priority matching
- **`pm-tracking.js`** — Rewrote handler to use new config table (with ListMappings fallback)
- **`api.js`** — Added `/api/pm-tracking-configs` CRUD routes
- **`index.html`** — Added "📋 Tracking Configs" card on PM Tracking page
- **`app.js`** — Added `loadPMTrackingConfigs()`, modal, toggle, delete

### Verification

#### PM Tracking Page — Configs + Tasks
![PM Tracking page with Tracking Configs section showing KABAM config (Active) and tasks table below](C:\Users\dangt\.gemini\antigravity\brain\498a5097-5772-44aa-8cbe-c02dec9cd185\pm_config_active_1773154374184.png)

#### Add PM Config Modal
![Modal with Title, ClickUp Type (List/Folder/Space), ClickUp ID, Job Type, Status fields](C:\Users\dangt\.gemini\antigravity\brain\498a5097-5772-44aa-8cbe-c02dec9cd185\pm_config_modal_1773154329845.png)

#### Pause Toggle Working
![KABAM config shown in Paused state with dimmed row](C:\Users\dangt\.gemini\antigravity\brain\498a5097-5772-44aa-8cbe-c02dec9cd185\pm_config_paused_1773154358326.png)

#### Demo Recording
![Browser verification recording](C:\Users\dangt\.gemini\antigravity\brain\498a5097-5772-44aa-8cbe-c02dec9cd185\pm_tracking_configs_1773154263242.webp)

### Commits
- `1bf0020` — feat: add pause/active toggle for List Configs + fix PM Tracking
- `9fd65e3` — feat: decouple PM Tracking with independent Space/Folder/List configs
