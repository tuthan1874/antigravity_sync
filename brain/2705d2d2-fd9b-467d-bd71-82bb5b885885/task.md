# Task Checklist

## Setup mappings
- [x] Create `ListMappings` table in NocoDB to map ClickUp List IDs to Slack Channels and Tagged Users.
- [x] Implement mapping lookup functions in `nocodb.js`.

## Task Creation Logic
- [x] Update `webhooks/clickup.js` to intercept `taskCreated`.
- [x] Look up list ID in `ListMappings`.
- [x] If mapped, send initial Slack message to create a thread.
- [x] Save the connection to `SyncConfigs` in NocoDB.

## Task Status Logic
- [x] Update `webhooks/clickup.js` to intercept `taskUpdated`.
- [x] If status changed to `CLIENT_REVIEW` or `client review`, look up `SyncConfigs` and `ListMappings`.
- [x] Send ping message to the Slack thread tagging the configured users.

## Task Deletion Logic
- [x] Update `webhooks/clickup.js` to intercept `taskDeleted`.
- [x] Look up `SyncConfigs` and delete the parent Slack message to remove the thread.
- [x] Delete or disable the `SyncConfigs` record.

## List Mappings UI
- [x] Backend: Create GET, POST, DELETE routes for `ListMappings` in `src/api.js`.
- [x] Frontend: Add a new navigation tab "List Mappings" in `public/index.html`.
- [x] Frontend: Add a data table to display existing mappings.
- [x] Frontend: Add an "Add Mapping" modal form in `public/app.js` to create new mappings.
- [x] Frontend: Implement `loadListMappings` and `deleteListMapping` JavaScript logic.
