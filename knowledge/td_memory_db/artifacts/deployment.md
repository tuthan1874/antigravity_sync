# Deployment and Configuration

The system is containerized for deployment on a Linux VPS.

## Docker Strategy
- **Base Image**: `python:3.11-slim`
- **Volume Persistance**:
    - `./data:/app/data`: To persist the SQLite message buffer and logs.
    - `./config:/app/config`: To allow hot-reloading `bot_roles.yaml` via the Admin UI.
- **Networking**: `network_mode: host` (or `extra_hosts`) to allow the container to access a self-hosted Qdrant on `localhost:6333`.

## Configuration Management
- **Environment Variables**: Managed via `.env` and `pydantic-settings`.
- **Bot Roles**: Defined in `config/bot_roles.yaml` as the source of truth for role identities and prompts.
- **Platform Tokens**: Follow the `{ROLE}_DISCORD_TOKEN` convention for easy discovery by the bot manager.

## Deployment Checklist
1. Pre-setup Qdrant collections using `scripts.setup_qdrant_collections`.
2. Configure LLM (CLIproxyAPI) and Embedder (OpenAI).
3. Set bot tokens in `.env`.
4. Deploy via `docker-compose up -d`.
5. Verify via Admin UI at `http://localhost:8500`.
