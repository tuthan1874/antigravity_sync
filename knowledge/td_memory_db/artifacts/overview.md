# TD Games Memory Database System Overview

The system is designed to create a "corporate memory" by capturing interactions across Discord and Slack, summarizing them into structured memories, and providing an AI-driven Q&A interface for company roles (CTO, CEO, PM, etc.).

## Key Features
- **Multi-Platform Support**: Discord (discord.py) and Slack (Slack Bolt Socket Mode).
- **Role-Based Bots**: Each bot corresponds to a company role with its own system prompt and Qdrant collection.
- **Mem0 Integration**: Uses `mem0` to normalize and store structured memories.
- **Daily Digest Pipeline**: Messages are buffered in SQLite and summarized daily by an LLM to extract "important info" for memory storage.
- **RAG-based Q&A**: Bots retrieve relevant memories from Qdrant to answer user @mentions in their specific persona.
- **Intent Detection & Task Flow**: LLM-based classifier routes @mentions to `QUERY`, `CREATE_TASK`, `UPDATE_TASK`, or `SET_REMINDER`.
- **Conversational flows**: A multi-turn `ConversationManager` handles stateful step-by-step gathering of task or reminder details.
- **ClickUp Integration**: Async integration for creating and updating tasks in ClickUp (TD_Workspace > Bot_Manager) with custom assignee fields.
- **Automated Reminders**: Persistent reminder system using `APScheduler` for one-time or recurring (daily/weekly) notifications.
- **Admin Web UI**: A FastAPI-based dashboard with a dark OLED UI for managing bots, roles, buffer, memories, and active reminders.
- **Auto-Provisioning**: Startup logic ensures ClickUp workspace and folders are correctly mapped to bot roles without manual configuration.

## Development Phases
The project evolved through several phases to reach completion:
1. **Core Engine**: `mem0` + Qdrant + basic Discord listener.
2. **Buffer & Roles**: Message buffer, `bot_roles.yaml`, and multiple bot support.
3. **Daily Digest**: Summarization engine for daily message processing.
4. **Slack Support**: Integration of Slack bots using Socket Mode.
5. **RAG Q&A**: Refined query engine for semantic search over memories.
6. **Deployment**: Dockerization and VPS configuration.
7. **Admin UI**: Building the FastAPI + HTML/JS dashboard.
8. **UI/UX Polishing**: Final polish of the dark OLED dashboard.
9. **Tasks & Reminders**: Implementation of `ClickUpClient`, `IntentDetector`, `ConversationManager`, and `ReminderManager`.
10. **Agent Persona & Memory Model**: Transition to an OpenClaw-inspired agent directory structure (`SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`) to provide persistent persona and context.
- **Language**: Python 3.11+
- **Memories**: [mem0](https://github.com/mem0ai/mem0)
- **Vector DB**: Qdrant (Self-hosted)
- **Bots**: discord.py, slack-bolt
- **Backend API**: FastAPI
- **LLM**: CLIproxyAPI (OpenAI-compatible) for chat/summarization using **gpt-5.2**, and official OpenAI for embeddings using **text-embedding-3-small**.
- **Database**: SQLite (Message buffer)
- **Scheduling**: APScheduler
