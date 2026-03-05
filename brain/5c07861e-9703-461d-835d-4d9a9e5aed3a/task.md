# Fix Drive Sync Duplicate Bug

- [x] Analyze root cause of Studio having more files than Client
- [x] Implement fixes in `sync.js`
  - [x] Fix 1: Stamp `sourceId` on name-matched files (legacy fallback)
  - [x] Fix 2: Stamp `sourceId` on name-matched folders
  - [x] Fix 3: Add duplicate detection + cleanup in mirror delete step
- [x] Verify the fix
