# Drive Sync Direction Feature Implementation Plan

The user requested adding the "Client \u2192 Studio" sync direction. During investigation, it was discovered that:
1. The frontend (`app.js`) currently only has `studio\u2192client` and `bidirectional` options.
2. The backend (`sync.js`) completely ignores the `Sync_Direction` field and always performs a one-way `Studio \u2192 Client` sync.
3. Implementing a naive `bidirectional` sync will cause an infinite loop of file copies (ping-pong effect) because when a file is copied, the new copy gets a fresh `modifiedTime` in Google Drive, making it appear "newer" than the source during the reverse sync pass.

## Proposed Changes

### 1. Backend (`src/drive/sync.js`)
- **Fix List Files**: Add `md5Checksum` to the Drive API `fields` requested in `listFiles()`.
- **Fix Ping-Pong Effect**: In `syncFolder()`, before deciding to update a file because it is "newer", check if `sourceFile.md5Checksum === existing.md5Checksum`. If they match, skip the copy to prevent infinite loops.
- **Implement Directions**: In `runDriveSync()`, add conditional logic based on `cfg.Sync_Direction`:
  - `studio\u2192client`: `syncFolder(cfg.Studio_Folder_ID, cfg.Client_Folder_ID)`
  - `client\u2192studio`: `syncFolder(cfg.Client_Folder_ID, cfg.Studio_Folder_ID)`
  - `bidirectional`: Run both `syncFolder(Studio, Client)` and `syncFolder(Client, Studio)`.
- **Log Messages**: Update the success and error logging to reflect the actual direction of sync instead of hardcoding "Copied to Client Folder".

### 2. Frontend (`public/app.js`)
- Add the `<option value="client\u2192studio">Client \u2192 Studio</option>` to the `Sync_Direction` select dropdown in `openModal()`.
- Update the UI table generation so the direction label can display the new option nicely.

## Verification Plan
### Automated tests
- N/A, not using automated testing for this.

### Manual Verification
1. Open the UI, click "Add Drive Config" or edit an existing one. Look for the "Client \u2192 Studio" and "Bidirectional" dropdown options.
2. We can create test folders in the user's Drive if possible, but the user will likely test this on their actual workflow. We will run `node test-drive.js` if there's a test script, or manually trigger the cron job to verify it doesn't crash.
