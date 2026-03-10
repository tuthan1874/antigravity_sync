# Decouple PM Tracking — Independent Config by Space/Folder/List

## Problem
PM Tracking hiện phụ thuộc vào bảng `ListMappings` (List Configs). User muốn tạo bảng config riêng cho PM Tracking — có thể theo dõi theo **Space ID**, **Folder ID**, hoặc **List ID** một cách độc lập.

## Design

### ClickUp Task Data (từ webhook)
Khi nhận webhook, `getTask(task_id)` trả về:
```json
{
  "list": { "id": "901815849460" },
  "folder": { "id": "90181234567" },
  "space": { "id": "90180000001" }
}
```
→ Ta có cả 3 level để match config.

### Matching Logic
Khi nhận task event, handler sẽ tìm config theo thứ tự ưu tiên:
1. **List ID** match → cụ thể nhất
2. **Folder ID** match → tất cả list trong folder
3. **Space ID** match → tất cả folder/list trong space

---

## Proposed Changes

### NocoDB Schema

#### [NEW] Bảng `PM_Tracking_Configs`

| Column | Type | Mô tả |
|--------|------|--------|
| `Id` | ID (auto) | Primary key |
| `Title` | SingleLineText | Tên config (VD: "KABAM Art Tracking") |
| `ClickUp_Type` | SingleLineText | `space` / `folder` / `list` |
| `ClickUp_ID` | SingleLineText | ID của Space, Folder hoặc List |
| `Job_Type` | SingleLineText | `Art` / `Animation` |
| `Enabled` | SingleLineText | `Active` / `Paused` |

---

### Backend

#### [MODIFY] [pm-tracking.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/handlers/pm-tracking.js)
- Thay `findListMapping(listId)` bằng `findPMTrackingConfig(taskDeet)`
- Match theo `list.id` → `folder.id` → `space.id` (ưu tiên cụ thể nhất)
- Vẫn return `listMapping` (ko thay đổi) cho Slack/Discord handlers

#### [MODIFY] [nocodb.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/nocodb.js)
- Thêm functions: `getPMTrackingConfigs()`, `findPMTrackingConfig(taskDeet)`, `createPMTrackingConfig()`, `updatePMTrackingConfig()`, `deletePMTrackingConfig()`

#### [MODIFY] [api.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/api.js)
- Thêm CRUD routes: `GET/POST/PUT/DELETE /api/pm-tracking-configs`

---

### Frontend

#### [MODIFY] [index.html](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/index.html)
- Thêm section "PM Tracking Configs" vào trang PM Tracking (nút "+ Add PM Config")

#### [MODIFY] [app.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/app.js)
- Thêm `loadPMTrackingConfigs()`, `openModal('pm-config')`, toggle pause/active
- Hiển thị bảng configs phía trên bảng tasks

---

## Cleanup

#### ListMappings — giữ nguyên `Job_Type` + `Enabled`
Cột `Job_Type` trên `ListMappings` sẽ **không còn được dùng** cho PM Tracking (vì đã tách ra). Có thể xóa sau nếu muốn, nhưng cột `Enabled` vẫn hữu ích cho Slack/Discord automation.

---

## Verification
1. Tạo PM Config với `ClickUp_Type=space`, nhập Space ID → verify tất cả task trong space đó được track
2. Tạo PM Config với `ClickUp_Type=list`, nhập List ID → verify chỉ task trong list đó được track
3. Pause config → verify task mới không được track
4. PM Tracking page hiển thị cả config table + task table
