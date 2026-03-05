# Drive Sync Duplicate Bug Fix

## Vấn đề
Khi sync Drive ở chế độ **Client → Studio**, folder Studio có nhiều file/folder hơn Client. Nguyên nhân: file/folder đã tồn tại ở Studio (cùng tên với Client) không được gắn `sourceId` → các lần sync sau tạo bản copy mới thay vì dùng file cũ, và mirror delete không xóa được bản gốc thừa.

## Thay đổi

### [sync.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js)

render_diffs(file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js)

### 3 Fix áp dụng:

| Fix | Mô tả | Dòng |
|-----|--------|------|
| **Stamp sourceId (Folders)** | Khi folder match bằng tên (không có sourceId), tự động gán `appProperties.sourceId` | 138-150 |
| **Stamp sourceId (Files)** | Tương tự cho files | 167-179 |
| **Duplicate Cleanup** | Re-scan dest sau STEP 1, phát hiện file duplicate (cùng sourceId hoặc file gốc trùng tên nhưng đã có tracked copy), tự động trash | 219-295 |

## Cách hoạt động sau fix

1. **Lần sync đầu**: File "Superman" ở Studio match bằng tên → được gán `sourceId` → từ nay trở đi track bằng ID chính xác
2. **Lần sync sau**: Match chính xác bằng `sourceId` → không tạo duplicate
3. **Dọn dẹp**: Nếu đã tồn tại duplicate từ trước, STEP 2 phát hiện và trash bản thừa

## Verification
- File `sync.js` đã được review toàn bộ, logic đúng và không ảnh hưởng đến các direction khác (`studio→client`, `bidirectional`)
- Bạn cần chạy `node test-drive.js` để verify trên data thực
