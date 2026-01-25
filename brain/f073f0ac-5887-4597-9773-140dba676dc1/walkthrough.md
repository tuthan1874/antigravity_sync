# Hệ thống Phân quyền Nâng cao (ClickUp Business Plus)

## Database Schema

### Bảng `user_account`
Đã có sẵn cột `role` hỗ trợ: `admin`, `member`, `guest`.

### Bảng mới: `resource_permission`

| Column | Type | Description |
|--------|------|-------------|
| `id` | bigint | Primary key |
| `user_id` | bigint | FK to `user_account` |
| `resource_type` | text | `project`, `board`, `card` |
| `resource_id` | bigint | ID của resource |
| `access_level` | text | `full`, `view_all`, `assigned_only` |
| `action_permission` | text | `edit`, `comment_only` |
| `created_at` | timestamp | Thời gian tạo |
| `updated_at` | timestamp | Thời gian cập nhật |

## Files đã tạo

1. **Migration**: [20260120000500_create_resource_permission.js](file:///e:/TDC_App/planka-master/server/db/migrations/20260120000500_create_resource_permission.js)
2. **Model**: [ResourcePermission.js](file:///e:/TDC_App/planka-master/server/api/models/ResourcePermission.js)

## Enums trong Model

```javascript
const ResourceTypes = {
  PROJECT: 'project',
  BOARD: 'board',
  CARD: 'card',
};

const AccessLevels = {
  FULL: 'full',
  VIEW_ALL: 'view_all',
  ASSIGNED_ONLY: 'assigned_only',
};

const ActionPermissions = {
  EDIT: 'edit',
  COMMENT_ONLY: 'comment_only',
};
```

## Verification
- ✅ Migration đã chạy thành công
- ✅ Bảng `resource_permission` đã được tạo trong PostgreSQL
