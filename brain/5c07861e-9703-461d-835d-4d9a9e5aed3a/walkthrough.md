# Drive Sync — Bug Fix + Safety Mechanisms

## Thay đổi trong [sync.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js)

render_diffs(file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js)

## Tổng kết thay đổi

### 1. Fix Duplicate Bug ✅
File/folder match bằng tên (legacy) giờ được gắn `sourceId` → không tạo duplicate sau này.

### 2. Client Folder Protection 🛡️ ✅
- `studio→client`: Copy file sang Client, **KHÔNG bao giờ xóa** file Client (`protectDest: true`)
- `bidirectional`: Copy cả 2 chiều, **CHỈ mirror-delete ở Studio** (Client luôn được bảo vệ)

### 3. Delete Threshold (50%) 🚨 ✅
Nếu STEP 2 phát hiện cần xóa **>50% file** ở destination → **dừng sync**, log cảnh báo vào NocoDB.

### 4. Audit Log 📝 ✅
Mọi thao tác xóa đều được log vào NocoDB (`SyncMessages`) với lý do cụ thể.

## Bảng tổng hợp behavior

| Direction | Copy | Mirror Delete | Client Protected |
|-----------|------|---------------|:---:|
| `studio→client` | Studio → Client | ❌ Không xóa | ✅ |
| `client→studio` | Client → Studio | ✅ Xóa Studio thừa | N/A |
| `bidirectional` | Cả 2 chiều | ✅ Chỉ xóa ở Studio | ✅ |

## Verification
- `test-drive.js` chạy thành công (exit code 0)
- Log cho thấy `🛡️ Skipping mirror delete (destination protected)` khi sync tới Client
