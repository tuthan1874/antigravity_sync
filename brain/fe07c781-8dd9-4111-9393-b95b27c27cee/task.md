# Add Discord to List Mappings

## Changes
- [x] Add `Discord_Channel_ID` and `Discord_Review_User_IDs` columns to NocoDB ListMappings table
- [x] Update frontend table display in `app.js` to show Discord columns
- [x] Update frontend modal form in `app.js` to include Discord fields
- [x] Create `discord-automation.js` handler (mirrors `slack-automation.js` for Discord threads)
- [x] Wire up `discord-automation.js` in `clickup.js` webhook handler
- [ ] Verify via browser that the UI works correctly
