# Session Walkthrough — 2026-03-11

## Completed Tasks

### 1. Git Push & GitHub Actions CI/CD
- Pushed pending commit to GitHub
- Created `.github/workflows/deploy.yml` — auto-deploy to VPS on push to `main`
- Deploy script: SSH → `git fetch --all && git reset --hard origin/main` → `npm install` → `systemctl restart chatsync`
- Created `deploy.sh` convenience script for local use
- User added 4 GitHub Secrets: `VPS_HOST`, `VPS_USER`, `VPS_PASSWORD`, `VPS_PORT`

### 2. Invoice Dual Currency (VNĐ/USD)
- **Summary bar**: handles mixed currencies — shows separate VNĐ and USD totals if both exist
- **Per-assignee cards**: each shows 🇻🇳 VNĐ or 🇺🇸 USD flag based on `inv.currency`
- Currency determined by NocoDB `PM_Tasks_Tracking.Currency` field

### 3. TD Games Logo
- Saved logo to `public/td-games-logo.png`
- **Sidebar**: replaced ⚡ emoji with actual logo image
- **Login page**: replaced ⚡ emoji with actual logo image
- **Invoice header**: added white logo alongside assignee name

### 4. Invoice Notes & Bonus Notes Columns
- Added 2 new columns to invoice table: **Bonus Note** (`t.Bonus_Reason`) and **Notes** (`t.Notes`)
- Table now has 9 columns: `# | Task Name | Type | Closed | Cost | Bonus | Bonus Note | Notes | Subtotal`
- Added `overflow-x: auto` + `min-width: 900px` for horizontal scroll support

### 5. Deploy Fixes
- **Cache fix**: Added `no-cache` middleware in `server.js` for `.js` and `.css` files
- **Deploy fix**: Changed `git pull` to `git fetch --all && git reset --hard origin/main` to prevent silent merge failures

## Key Files Modified
| File | Changes |
|------|---------|
| [deploy.yml](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/.github/workflows/deploy.yml) | CI/CD workflow with force-sync deploy |
| [server.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/server.js) | No-cache headers for JS/CSS |
| [index.html](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/index.html) | Logo in sidebar + login |
| [app.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/app.js) | Invoice: dual currency, logo, Notes columns |
| [td-games-logo.png](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/td-games-logo.png) | TD Games logo asset |

## Lessons Learned
- VPS `git pull` can fail silently when working tree is dirty — always use `git reset --hard`
- Express default static serving allows aggressive browser caching — add no-cache headers for dev assets
- App URL: **https://sync.tdgamestudio.com/** (behind Nginx reverse proxy with SSL)
- VPS port 3000 is Open WebUI, ChatSync runs on a different port proxied by Nginx
