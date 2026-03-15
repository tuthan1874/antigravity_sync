# Workforce App — ClickUp Sync — Session 15/03/2026

## Tổng quan phiên làm việc

Tích hợp **ClickUp sync** vào Workforce app: task chỉ đồng bộ từ ClickUp (không tạo thủ công), match bằng email assignee.

---

## Đã hoàn thành ✅

### 1. Database
- Tạo bảng `wf_clickup_config` (token, team_id, spaces/lists, last_synced)
- Fix FK constraints: `wf_tasks` + `wf_settlements` → `ON DELETE CASCADE` (cho phép xóa worker)

### 2. Edge Function `clickup-sync`
- Deploy thành công, 4 actions: `get_teams`, `get_spaces`, `get_lists`, `sync_tasks`
- Proxy ClickUp API qua Supabase Edge Function (giấu token)

### 3. Frontend

| File | Thay đổi |
|---|---|
| [clickupService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/services/clickupService.ts) | NEW — gọi Edge Function + CRUD config |
| [ClickUpConfig.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/ClickUpConfig.tsx) | NEW — wizard: Token → Team → auto-load ALL Spaces & Lists |
| [TaskList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/TaskList.tsx) | Xóa form thủ công, thêm Sync button, bỏ nút xóa task |
| [WorkerList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/WorkerList.tsx) | Fix nút xóa: custom inline confirm thay vì `window.confirm()` |
| [WorkforceApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/WorkforceApp.tsx) | Thêm tab CẤU HÌNH |
| [useWorkforceState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/hooks/useWorkforceState.ts) | Thêm 'config' tab type |

### 4. Bug fixes
- Fix nút xóa worker bị che bởi status dot → dời dot xuống inline
- Thay `confirm()` bằng custom overlay trên card
- Fix FK constraint chặn xóa worker có tasks

---

## Cần làm tiếp 🔜

1. **Test ClickUp sync thực tế** — nhập Personal API Token (`pk_...`) → chọn team → sync tasks
2. **Kiểm tra xóa nhân sự** — xác nhận fix inline confirm hoạt động OK
3. **Phase 3**: Auto-tạo Expense record khi settlement được thanh toán
4. **Cải thiện UX**: hiển thị giá task, filter nâng cao, export báo cáo
