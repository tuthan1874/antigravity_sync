# Slack Auto-Threading Sync from ClickUp

This plan details the implementation of full workflow automation between ClickUp and Slack directly within our Node.js application, eliminating the need for external triggers like N8N. 

## User Review Required

> [!IMPORTANT]
> The automation relies on a newly proposed `ListMappings` table in NocoDB. Please confirm if you are comfortable with this new table approach to manage where alerts are sent:
> - **List_ID**: The ID of the ClickUp List (e.g., `901815849460` for Art).
> - **Slack_Channel_ID**: The ID of the Slack Channel to thread the tasks in.
> - **Slack_Review_User_IDs**: Slack User IDs to tag when the status changes to CLIENT_REVIEW (e.g., `<@U123456>`).
> - **Customer_Id** & **Project_Id**: Link fields so this auto-sync syncs directly to your structured log filters.

## Proposed Changes

---

### Database Schema (NocoDB)

#### [NEW] `create-list-mapping-table.js`
A new script to programmatically build the `ListMappings` table in NocoDB. This gives the app a dynamic lookup point: allowing you to configure exactly which ClickUp list threads into which Slack channel and who gets pinged without hardcoding IDs in the future.

#### [MODIFY] `src/nocodb.js`
Extend the existing database wrappers to include functions for reading `ListMappings`, as well as creating or deleting `SyncConfigs` programmatically.

---

### Core Automation Logic (ClickUp Webhook)

#### [MODIFY] `src/webhooks/clickup.js`
We will expand the event listener block for `taskCreated`, `taskUpdated`, and `taskDeleted`:

1.  **Handling `taskCreated`:**
    - Look up the `List_ID` in `ListMappings`.
    - If a mapping is found, use the Slack API to broadcast the text: `"🆕 New Task Created: [Task Name] (URL)"` to the mapped `Slack_Channel_ID`.
    - Retrieve the newly created Slack message's timestamp (`ts`).
    - Save a new record into `SyncConfigs` specifying two-way sync: `Sync_ClickUp_To_Slack=true`, `Sync_Slack_To_ClickUp=true`.

2.  **Handling `taskUpdated`:**
    - Check if the payload indicates a status change to `CLIENT_REVIEW` (or similar configured variant).
    - If so, look up `SyncConfigs` to find the exact Slack Thread `ts`.
    - Look up `ListMappings` for the Slack User IDs to tag.
    - Post an automated message directly to the Slack Thread: `"🔔 Please review this task: <@UserId> (URL)"`.

3.  **Handling `taskDeleted`:**
    - Look up `SyncConfigs` for the mapped Slack Thread.
    - Delete the origin message on Slack (which deletes the entire thread).
    - Delete the `SyncConfigs` record to clean up the database routing.

---

### Slack API Integration

#### [MODIFY] `src/platforms/slack-api.js`
Add helper functions to:
- Delete a Slack message by `ts`.
- Send initial top-level messages to a channel without threading logic (to generate the thread entry point constraint).

## Verification Plan
1. Send a manual `taskCreated` payload and ensure Slack receives the base message and the `SyncConfigs` record initializes successfully.
2. Send a manual `taskUpdated` payload moving the status to `CLIENT_REVIEW` and observe the automated ping inside the thread. 
3. Send a manual `taskDeleted` payload and confirm the thread is nuked from Slack and NocoDB is clean.
