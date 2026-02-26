# Hierarchy Management & Log Filters

We will upgrade the application to support a hierarchical structure (`Customer -> Project -> Sync/Drive Configs`) to better organize different sync configurations. Furthermore, we will upgrade the UI to display and filter sync logs by this hierarchy.

## User Review Required

> [!IMPORTANT]
> The database schema will be automatically modified by the AI using the NocoDB MCP server. We will create two new tables (`Customers` and `Projects`) and add relationship columns (`Customer_Id` and `Project_Id`) to existing tables. No manual database setup will be required from you.

## Proposed Changes

### Database Schema Updates (via MCP)
- **Create `Customers` table**: `Title` (SingleLineText)
- **Create `Projects` table**: `Title` (SingleLineText), `Customer_Id` (Number)
- **Modify `SyncConfigs`**: Add `Project_Id` (Number)
- **Modify `DriveConfigs`**: Add `Project_Id` (Number)
- **Modify `SyncMessages`**: Add `Project_Id` (Number), `Customer_Id` (Number)

### Backend Updates
#### [MODIFY] `src/nocodb.js`
- Implement `getCustomers`, `createCustomer`, `updateCustomer`, `deleteCustomer`.
- Implement `getProjects`, `createProject`, `updateProject`, `deleteProject`.
- Update `logMessage` to accept and insert `Customer_Id` and `Project_Id`.
- Update `getRecentMessages` to support `where` clauses (for filtering by Customer, Project, or SyncConfig).

#### [MODIFY] `src/api.js`
- Expose REST API endpoints for `/api/customers` and `/api/projects`.
- Update `/api/sync-messages` to parse query parameters (`customerId`, `projectId`, `syncConfigTitle`) and pass them to the NocoDB fetcher.

#### [MODIFY] `src/relay.js` & `src/drive/sync.js`
- Ensure that when a message is logged or a drive sync result is logged, the respective `Customer_Id` and `Project_Id` from the config are included.

### Frontend Updates
#### [MODIFY] `public/index.html`
- Add navigation links for **"Customers"** and **"Projects"**.
- Add pages (divs) to display Customers and Projects tables, mimicking the design of Sync Configs.
- Update the **"Logs"** page to include a filter bar: Dropdowns for Customer, Project, and Task/Config.

#### [MODIFY] `public/app.js`
- Implement frontend state and API calls to manage Customers and Projects.
- Inject a "Project" `<select>` dropdown in the "Add Sync Config" and "Add Drive Config" modals.
- Implement cascaded dropdowns in the Logs page (Selecting a customer filters the projects; selecting a project fetches its logs).

## Verification Plan

### Automated Tests
- Restart the backend to ensure no compilation errors.

### Manual Verification
1. Open the UI, navigate to "Customers" and create a test customer.
2. Navigate to "Projects", create a test project under the new customer.
3. Edit an existing Sync Config to assign it to the new project.
4. Send a test message in Discord/Slack and verify it relays successfully.
5. Go to the "Logs" page, select the Customer, and verify the log appears and filters correctly.
