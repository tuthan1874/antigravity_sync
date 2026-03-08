# Admin Web UI

A specialized management dashboard built using the **UI/UX Pro Max** design system.

## Frontend Design
- **Theme**: Dark OLED (#020617 background, #22C55E green accents).
- **Typography**: Fira Code (Technical/Stats) and Fira Sans (Body).
- **Architecture**: Single Page Application (SPA) using Vanilla JS (no heavy frameworks).
- **Navigation**: Sidebar with SVG icons.
- **Components**: Stat cards, data tables, modal role editors, and semantic search interfaces.

## Backend (FastAPI)
- **Mounting**: Mounted as a FastAPI app within the main bot process.
- **REST Endpoints**:
    - `GET /api/dashboard`: Aggregate stats from SQLite and Qdrant.
    - `GET/POST/PUT/DELETE /api/roles`: CRUD for `bot_roles.yaml`.
    - `GET /api/buffer/messages`: Browse raw chat logs.
    - `POST /api/digest/trigger`: Manually run the summarization job for a date.
    - `POST /api/memories/{role}/search`: Test semantic search results.
    - `GET /api/reminders`: List all active scheduled reminders (filter by role/user).
    - `DELETE /api/reminders/{id}`: Cancel a specific reminder by ID.

## Features
- **Dashboard Overview**: Key stats (total/today's messages, unprocessed count), live bot status, and Qdrant collection health.
- **Reminders Management**: Built-in interface to view and manage upcoming system notifications.
- **ClickUp Status**: Indicates if the integration is enabled globally and if each role has a target List ID configured.
- **Bot Manager**: Interactive CRUD for updating bot personas and configuration directly in `bot_roles.yaml`.

## Shared Context
The FastAPI app shares a global `_app_context` dictionary set by `main.py`, allowing it to access the live bot status, memory engines, and database connections.
