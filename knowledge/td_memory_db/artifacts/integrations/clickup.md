# ClickUp Integration

The system manages tasks on ClickUp within the **TD_Workspace** (Space) and **Bot_Manager** (Folder). Each bot role is associated with a specific List.

## Features
- **Task Creation**: Creates tasks with name, description, priority, and dates.
- **Custom Assignment**: Instead of native ClickUp assignment (which requires users to be in ClickUp), user details are stored in custom fields:
  - `Assignee Name` (Short Text): The display name of the user who requested the task.
  - `Assignee ID` (Short Text): The unique platform ID formatted as `platform:user_id` (e.g., `discord:123456789012` or `slack:U05ABC123`). This allows the bot to uniquely identify and @mention the user on the correct platform for reminders.
- **Auto-Extraction**: When a user @mentions someone in the task creation flow (e.g., "Assign cho @user"), the bot automatically extracts both the display name and the platform-specific ID to populate these fields.
- **Status Management**: Supports updating status (done, pending, in progress) via conversational commands by searching the current list for matching task names or IDs.
- **Date Handling**: LLM handles natural language date parsing (e.g., "ngay mai 2h chieu") before sending ISO timestamps to ClickUp, using the bot's current system time as context.

## Implementation Details
The `ClickUpClient` (`core/clickup_client.py`) is an async wrapper using `aiohttp`.

### Core Methods:
- `create_task(...)`: `POST /list/{list_id}/task`
- `update_task(...)`: `PUT /task/{task_id}`
- `set_custom_field(...)`: `POST /task/{task_id}/field/{field_id}`
- `get_list_tasks(...)`: `GET /list/{list_id}/task`

## Config
- `CLICKUP_API_TOKEN`: Personal token for API access.
- `CLICKUP_SPACE_ID`: Fixed ID for the ClickUp Space (e.g., `TD_Workspace`).
- `CLICKUP_FOLDER_ID`: Fixed ID for the ClickUp Folder (e.g., `Bot_Manager`).
- `clickup_list_id`: Target list for each role in `bot_roles.yaml` (auto-populated by provisioner).
- `clickup_assignee_name_field_id`: ID of the custom field for the assignee's display name (auto-detected).
- `clickup_assignee_id_field_id`: ID of the custom field for the assignee's platform-specific ID (auto-detected).

## Auto-Provisioning Logic
To minimize manual setup, the system performs an auto-provisioning flow at startup if `CLICKUP_API_TOKEN` is set:
1. **Target Identification**: Uses the fixed `CLICKUP_SPACE_ID` and `CLICKUP_FOLDER_ID` from the environment.
2. **List Discovery**: For each bot role (TD_CTO, TD_CEO, etc.), it searches for a List named exactly after the `role_id`.
3. **List Creation**: If a List for that role does not exist, it creates one inside the fixed Folder.
4. **Field Provisioning**: Automatically detects or creates the **Assignee_Name** and **Assignee_ID** short-text custom fields for each list.
5. **Persistence**: The resulting `list_id` is automatically saved back to `config/bot_roles.yaml` and the field IDs are mapped in-memory to the role configurations.

This ensures that adding a new bot in `bot_roles.yaml` and restarting the application will automatically create the corresponding ClickUp structure.

