# Run Project

- [x] Install dependencies (`npm install`)
- [x] Start the project (`npm run dev`)

## OAuth 2.0 Migration
- [x] Update `.env` requirements and `src/config.js`
- [x] Create `src/drive/auth.js` for OAuth handling
- [x] Update `src/drive/sync.js` to use OAuth client and NocoDB tokens
- [x] Add auth routes to `src/api.js`
- [x] Manual User Authentication (Login Flow)
- [x] Verify sync works

## Hierarchy Management & Log Filters
- [x] Create `Customers` and `Projects` tables in NocoDB via MCP
- [x] Add `Customer_Id` and `Project_Id` columns to respective tables
- [x] Implement Backend CRUD for Customers and Projects (`nocodb.js`, `api.js`)
- [x] Update `relay.js` and `drive/sync.js` to log hierarchy IDs
- [x] Implement Frontend UI for managing Customers and Projects (`index.html`, `app.js`)
- [x] Implement Log Filtering UI on the Frontend
