# Code Review Fixes — Walkthrough

## 12 of 13 issues fixed across 8 files

### P0 — Critical ✅

**#1 Debug log removed** — [slack.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/webhooks/slack.js)
- Removed `appendFileSync` that wrote every Slack payload to disk infinitely

**#9 Race condition fixed** — [server.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/server.js)
- Added `isDriveSyncing` / `isCheckingReminders` mutex locks
- Changed cron callbacks to `async` with proper `await`
- Added `try/catch/finally` for error resilience

---

### P1 — Important ✅

**#2 JWT secret required** — [auth.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/middleware/auth.js)
- Removed hardcoded fallback `'chatsync-secret-key-123!@#'`
- Server crashes on startup if `JWT_SECRET` missing from `.env`

**#3 Password hashing** — [api.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/api.js)
- Added `bcryptjs` for password comparison
- Supports both bcrypt hashed and legacy plaintext (backward compatible)
- Proper `!passwordValid` rejection added

**#6 Hardcoded List IDs removed** — [clickup.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/webhooks/clickup.js)
- Replaced `listId === '901815849460'` with `listMapping?.Job_Type` from NocoDB
- New lists can be added via NocoDB without code changes

**#8 Reminders persisted to NocoDB** — [reminders.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/jobs/reminders.js)
- Removed file-based `.data_reminders.json`
- Now uses NocoDB Settings table (`Title: reminder_{taskId}`)
- Survives server restarts / redeployments

---

### P2 — Improvements

**#7 Drive API retry** — [sync.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/src/drive/sync.js)
- Added `withRetry()` helper with exponential backoff (1s → 2s → 4s, max 10s)
- Handles 429 (rate limit), 500/503, ECONNRESET, ETIMEDOUT
- Applied to `listFiles`, `copyFile`, `createFolder`

**#4 + #11 .gitignore updated** — [.gitignore](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/.gitignore)
- Added: `.data_reminders.json`, `slack_debug_payloads.log`, `*.txt`, `tmp_*.json`

**#5 ClickUp handler refactoring** — ⏸️ Deferred (structural change, risk of breaking)

---

### P3 — Nice-to-have ✅

| Fix | File |
|-----|------|
| #10 `.env.example` created | [.env.example](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/.env.example) |
| #12 CORS restricted | [server.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/server.js) |
| #13 Health check improved | [server.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/server.js) |

---

## Verification
All 8 modified files pass `node --check` syntax validation ✅

> [!IMPORTANT]
> Password hash migration: Current passwords vẫn hoạt động (plaintext fallback). Khi cần, dùng `bcryptjs.hashSync(password, 10)` để tạo hash rồi cập nhật vào NocoDB.
