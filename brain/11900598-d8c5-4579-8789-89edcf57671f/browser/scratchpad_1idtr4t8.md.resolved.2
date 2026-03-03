# Bank Profile Management Test Checklist

- [x] Open Bank Manager panel (gear icon ⚙️)
- [x] Verify existing banks and icons (Edit/Delete) are visible
- [x] Edit an existing bank (change alias)
- [f] Save changes and verify update (FAILED - NocoDB 404)
- [x] Add a new bank (Test Bank)
- [f] Verify new bank is added to the list (FAILED - NocoDB 404)
- [x] Check for console errors throughout (Found 404 ERR_BASE_NOT_FOUND)

### Findings
- Bank Manager UI is fully implemented: Add, Edit, Delete (always visible icons).
- Existing bank "Techcombank V2" detected, but its ID seems to be a local fallback (`local_...`).
- Inline edit form correctly pre-fills and allows typing.
- **CRITICAL**: All Save/Update/Fetch operations to NocoDB are failing with:
  `404 {"error":"ERR_BASE_NOT_FOUND","message":"Base '_' not found"}`.
- This suggests the `NOCODB_BASE_ID` is missing or the API URL construction in `nocodbService.ts` is using `_` as a placeholder that isn't being replaced or handled correctly by the server.
- Studio Info section is also present and editable, but lacks a dedicated "Save" button in the UI (might be intended to save with the invoice).
