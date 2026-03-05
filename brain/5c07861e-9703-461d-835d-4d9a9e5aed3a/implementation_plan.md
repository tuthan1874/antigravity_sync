# Drive Sync Bug: Studio folder có nhiều file hơn Client khi sync "Client → Studio"

## Phân tích nguyên nhân gốc

Sau khi đọc kỹ `sync.js`, tôi đã tìm thấy **2 lỗi chính** khiến folder Studio có nhiều file/folder hơn Client khi đặt chế độ `client→studio`.

---

### 🐛 Bug 1: Mirror Delete logic kiểm tra sai hướng (CRITICAL)

> [!CAUTION]
> Đây là lỗi chính gây ra vấn đề.

Tại [sync.js dòng 192-236](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js#L192-L236), STEP 2 (Mirror Delete) kiểm tra file thừa ở **destination** bằng cách đối chiếu với **source** files.

**Tuy nhiên**, logic này kiểm tra bằng `sourceIds` — là danh sách ID của source files — trong khi `destFile.appProperties.sourceId` lưu ID của **file gốc** (file ở source mà đã được copy sang). 

**Vấn đề cụ thể:**

```javascript
// Dòng 193: sourceIds chứa các ID FILE GỐC ở source folder
const sourceIds = new Set(sourceFiles.map(f => f.id));

// Dòng 202-205: Kiểm tra destFile.appProperties.sourceId có NẰM TRONG sourceIds không
if (destFile.appProperties && destFile.appProperties.sourceId) {
    if (!sourceIds.has(destFile.appProperties.sourceId)) {
        shouldTrash = true; // ← Đúng logic: sourceId trỏ tới file gốc, kiểm tra file gốc còn tồn tại không
    }
}
```

Logic ID-tracking này **đúng**. Nhưng vấn đề là ở phần **legacy fallback (dòng 206-210)**:

```javascript
else {
    // Legacy untracked files: Check if name is gone
    if (!sourceNames.has(destFile.name)) {
        shouldTrash = true;
    }
}
```

**Khi một file ở destination KHÔNG có `appProperties.sourceId`** (vì nó là file gốc của folder đó, không phải file được copy từ sync), thì code fallback để kiểm tra theo tên. Điều này có nghĩa là:

- **Các file thủ công** mà Studio tạo riêng (không liên quan đến sync) mà **trùng tên** với file của Client → sẽ KHÔNG bị xóa (đúng)
- **Các file thủ công** mà Studio tạo riêng mà **khác tên** với file Client → sẽ BỊ XÓA (đúng cho mirror mode)

**Nhưng thực tế:** Khi Studio folder **là destination** và có chứa file gốc (file đã tồn tại trước khi sync), những file này không có `sourceId` → fallback theo tên → chỉ xóa nếu tên không trùng với source.

⚠️ **Vấn đề thực sự nằm ở chỗ khác:**

Khi direction = `client→studio`:
- `syncFolder(Client_Folder_ID, Studio_Folder_ID)` được gọi
- Source = Client, Dest = Studio
- STEP 1: Copy file từ Client → Studio ✅
- STEP 2: Xóa file ở Studio mà Client không có ✅

**Logic trên thực ra đúng!** Vậy lỗi phải ở chỗ khác...

---

### 🐛 Bug 2: `name_` key mapping có thể tạo duplicate (ROOT CAUSE)

> [!CAUTION]
> Đây chính là nguyên nhân gốc tạo ra file thừa.

Tại [sync.js dòng 91-100](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js#L91-L100):

```javascript
const destMap = new Map();
for (const f of destFiles) {
    if (f.appProperties && f.appProperties.sourceId) {
        destMap.set(`id_${f.appProperties.sourceId}`, f);
    } else {
        destMap.set(`name_${f.name}`, f);
    }
}
```

Và tại [dòng 118](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js#L118):

```javascript
let existing = destMap.get(`id_${sourceFile.id}`) || destMap.get(`name_${sourceFile.name}`);
```

**Kịch bản gây lỗi:**

1. **Lần sync đầu tiên**: Client có file "Superman". Sync chạy, copy "Superman" sang Studio với `appProperties.sourceId = <client-file-id>`. ✅
2. **Studio đã có sẵn file "Superman"** (file gốc, không có `sourceId`). Lần đầu sync, `destMap` sẽ có:
   - `name_Superman` → file gốc (vì không có sourceId)
   - Code tìm `existing` = `destMap.get(`id_${sourceFile.id}`)` → **null** (vì file gốc không có sourceId match) → fallback `destMap.get(`name_Superman`)` → **tìm thấy** → skip copy ✅
3. **Lần sync thứ 2**: Studio giờ có **2 file "Superman"**: file gốc + file copy (với sourceId). `destMap` sẽ lưu:
   - `id_<client-id>` → file copy ✅
   - `name_Superman` → file gốc ✅
   - Code tìm `existing` = `destMap.get(`id_${sourceFile.id}`)` → **tìm thấy file copy** → skip ✅

**Nhưng ở STEP 2 (Mirror Delete):**
- File gốc "Superman" (không có sourceId) → fallback tên → `sourceNames.has("Superman")` → true → **KHÔNG bị xóa**
- File copy "Superman" (có sourceId) → `sourceIds.has(sourceId)` → true → **KHÔNG bị xóa**

→ **Kết quả: Studio có 2 file "Superman" trong khi Client chỉ có 1!** 🐛

### Tổng kết nguyên nhân

| Vấn đề | Giải thích |
|---|---|
| **File duplicate** | Khi Studio đã có file cùng tên trước khi sync, lần đầu match theo tên nên skip, nhưng file gốc vẫn tồn tại. Các lần sync sau match theo `sourceId` nên file gốc bị "mồ côi" — không bị xóa vì tên vẫn trùng |
| **Folder duplicate** | Tương tự — khi folder cùng tên tồn tại ở Studio, sync tạo thêm folder mới thay vì dùng folder đã có |

---

## Proposed Changes

### [MODIFY] [sync.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js)

#### Fix 1: Xử lý duplicate — khi tìm `existing` file/folder, nếu match bằng name thì **gắn `sourceId`** vào file destination để các lần sync sau không bị duplicate

Thêm logic: sau khi match bằng name (fallback), update `appProperties.sourceId` cho destination file đó → lần sync sau sẽ match bằng ID.

```diff
 if (!existing) {
     await copyFile(sourceFile.id, destFolderId, sourceFile.name);
 } else {
+    // If matched by name (legacy), stamp sourceId for future tracking
+    if (!existing.appProperties?.sourceId) {
+        try {
+            await driveService.files.update({
+                fileId: existing.id,
+                requestBody: { appProperties: { sourceId: sourceFile.id } },
+                supportsAllDrives: true,
+            });
+        } catch (e) { /* log warning */ }
+    }
```

#### Fix 2: Xử lý STEP 2 Mirror Delete — cải thiện logic để phát hiện và xóa file duplicate thừa

Sau STEP 1, re-scan destination files. Nếu có nhiều file cùng tên hoặc cùng sourceId, giữ lại file có `sourceId` và xóa file thừa.

#### Fix 3: Tương tự cho folders — khi match folder bằng name, gắn `sourceId` để tracking

---

## Verification Plan

### Manual Verification
- Bạn kiểm tra thủ công bằng cách:
  1. Chạy `node test-drive.js` để xem count file ở cả 2 folder trước khi fix
  2. Apply fix
  3. Chạy lại `node test-drive.js` → count file ở Studio phải = count file ở Client
  4. Kiểm tra trên Google Drive UI rằng Studio folder không còn file duplicate
