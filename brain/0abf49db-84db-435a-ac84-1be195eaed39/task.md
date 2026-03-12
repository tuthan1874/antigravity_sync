# Cascade Pause/Delete from ListMappings to SyncConfigs

## Tasks
- [x] Research codebase architecture (ListMappings, SyncConfigs, automation handlers)
- [x] Analyze NocoDB table schemas and data relationships
- [x] Write implementation plan
- [x] Add `List_Mapping_Id` column to SyncConfigs table in NocoDB
- [x] Update `slack-automation.js` to store `List_Mapping_Id` when creating SyncConfigs
- [x] Update `discord-automation.js` to store `List_Mapping_Id` when creating SyncConfigs
- [x] Add helper functions to `nocodb.js` (getSyncConfigsByListMappingId, bulkUpdateSyncConfigStatus, bulkDeleteSyncConfigs)
- [x] Update API: cascade pause/delete on `PUT /api/list-mappings/:id` and `DELETE /api/list-mappings/:id`
- [x] Backfill existing 12 SyncConfigs with `List_Mapping_Id=2` and `Status='paused'`
- [x] Verify all SyncConfigs are now paused
