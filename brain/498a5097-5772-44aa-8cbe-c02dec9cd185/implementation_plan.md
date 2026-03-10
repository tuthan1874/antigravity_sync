# List Configs Pause/Active + PM Tracking Fix

## Root Cause Analysis

### PM Tracking không hoạt động
Bảng `ListMappings` trong NocoDB **thiếu cột `Job_Type`**. Handler `pm-tracking.js` kiểm tra `listMapping?.Job_Type` — luôn trả về `undefined` → handler skip tất cả tasks, không sync gì vào `PM_Tasks_Tracking`.

### List Configs thiếu chức năng Pause/Active  
Bảng `ListMappings` không có cột `Enabled` hoặc `Status`. Không có cách nào tạm dừng (pause) một luồng auto-sync mà không xóa mapping.

---

## Proposed Changes

### NocoDB Schema (ListMappings table)

#### Add 2 new columns via MCP
1. **`Job_Type`** — `SingleSelect` với options: `Art`, `Animation`
2. **`Enabled`** — `SingleSelect` với options: `Active`, `Paused` (default: `Active`)

Sau đó update record KABAM/ORCA (Id=2) với `Job_Type=Art`, `Enabled=Active`.

---

### Backend Handler

#### [MODIFY] [pm-tracking.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/handlers/pm-tracking.js)
- Thêm check `listMapping?.Enabled === 'Paused'` → skip PM tracking nếu mapping bị paused

#### [MODIFY] [slack-automation.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/handlers/slack-automation.js)
- Thêm check `listMapping?.Enabled === 'Paused'` trước khi tạo thread/tag reviewers (line 30)

#### [MODIFY] [discord-automation.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/handlers/discord-automation.js)
- Thêm check `listMapping?.Enabled === 'Paused'` trước khi tạo thread/ping reviewers (line 31)

---

### Frontend UI

#### [MODIFY] [index.html](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/index.html)
- Thêm cột `Job Type` và `Status` vào table header (List Mappings, line 438-447)
- Cập nhật colspan từ 8 → 10

#### [MODIFY] [app.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/app.js)
- `loadListMappings()`: Hiển thị `Job_Type`, `Enabled` (status badge), và nút toggle ⏸️/▶️
- `openModal('list-mapping')`: Thêm select `Job_Type` (Art/Animation) và `Enabled` (Active/Paused)  
- Thêm function `toggleListMappingStatus(id, currentStatus)` gọi PUT API để đổi trạng thái

#### [MODIFY] [api.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/api.js)
- Route `PUT /api/list-mappings/:id` đã tồn tại → không cần thêm route mới

---

## Verification Plan

### Manual Verification
1. Start server: `node server.js` từ thư mục project
2. Mở browser → trang List Configs
   - Kiểm tra bảng hiển thị cột Job Type và Status
   - Nhấn nút toggle ⏸️ để pause → status đổi thành "Paused"
   - Nhấn nút toggle ▶️ để active lại → status đổi thành "Active"
3. Mở trang PM Tracking → kiểm tra dữ liệu hiện có vẫn hiển thị bình thường
4. Edit một List Mapping → kiểm tra modal có field Job Type và Enabled
