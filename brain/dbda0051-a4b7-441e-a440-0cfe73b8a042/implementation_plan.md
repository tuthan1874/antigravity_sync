# Directional Chat Sync

The user wants to configure directional paths for Chat Sync on a per-task basis (e.g., allow Discord ➔ ClickUp but block ClickUp ➔ Discord).

## Proposed Changes

### Database Schema Updates (via MCP)
Add the following `Checkbox` columns to the `SyncConfigs` table:
- `Sync_ClickUp_To_Slack`
- `Sync_ClickUp_To_Discord`
- `Sync_Slack_To_ClickUp`
- `Sync_Slack_To_Discord`
- `Sync_Discord_To_ClickUp`
- `Sync_Discord_To_Slack`

### Backend Updates
#### [MODIFY] `src/relay.js`
- Update the `getTargets` function.
- Before pushing a target platform into the list, read the boolean sync rules from `syncConfig`.
- If a rule is explicitly `false`, block that path. If `true` or `null` (backward compatibility), allow it.

### Frontend Updates
#### [MODIFY] `public/app.js`
- In `openModal('chat')`, add a configuration grid with 6 checkboxes for each directional path.
- In `handleFormSubmit`, intercept the `FormData`. Because unchecked checkboxes are not included in FormData, manually parse these 6 values into booleans (`=== 'on'`) before sending the POST/PUT payload to the NocoDB API.

## Verification
- We can create/edit a SyncConfig, toggle off Discord ➔ Slack, send a mock Discord message and ensure it goes to ClickUp but not Slack.
