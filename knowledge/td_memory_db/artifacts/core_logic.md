# Core Logic Patterns

## 1. Memory Engine (mem0 + Qdrant)
The system uses a `MemoryEngineManager` to handle separate collections for each role.

```python
# Implementation pattern in core/memory_engine.py
class MemoryEngineManager:
    def get_engine(self, role_id: str):
        # Initializing mem0 with Qdrant provider
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {"url": qdrant_url, "collection_name": f"{role_id}_memory"}
            },
            "llm": {"provider": "openai", "config": {"model": llm_model, "api_key": llm_key, "openai_base_url": llm_url}},
            "embedder": {"provider": "openai", "config": {"model": "text-embedding-3-small", "api_key": openai_key}}
        }
        return Memory.from_config(config)
```

## 2. Daily Digest Pipeline
Messages are processed in batches to save tokens and maintain context.

- **Grouping**: Messages are grouped by platform and channel name.
- **Batching**: Large message histories are split into chunks.
- **Summarization Prompt**: Uses a role-specific `digest_prompt` from `bot_roles.yaml`.
- **Noise Filtering**: If the LLM returns "NO_IMPORTANT_INFO", the batch is skipped to avoid cluttering memories.

## 3. Query Engine (RAG)
1. User @mentions bot with a question.
2. Query is embedded and searched against the role's Qdrant collection via `mem0.search()`.
3. Relevant memories are injected into the system prompt.
4. LLM generates a response in the role's persona.

## 4. Message Buffer Schema
SQLite table `messages`:
- `id`: Primary Key
- `role_tag`: Which bot should have "heard" this (optional)
- `platform`: `discord` or `slack`
- `channel_id`, `channel_name`
- `user_id`, `username`
- `content`: Raw message text
- `timestamp`: ISO timestamp
- `date_key`: YYYY-MM-DD (for grouping)
- `is_processed`: Boolean (True after digest run)

## 5. Application Startup Sequence
The `main.py` entry point follows a strictly ordered initialization to manage shared dependencies:
1. **Windows Encoding Fix**: Reconfigure `stdout/stderr` (if applicable).
2. **Settings & YAML Loading**: Load roles and environment variables.
3. **Shared Components**: Initialise the `MessageBuffer`, `MemoryEngineManager`, and `DailyDigest`.
4. **Phase 9 Core**: Initialise `IntentDetector`, `ConversationManager`, and `ReminderManager`. This must happen **before** the Admin UI starts so the API context has access to these services.
5. **Scheduler**: Setup and start the `APScheduler` (used for both digests and reminders).
6. **Admin Web UI**: Set the `_app_context` (sharing references to all core components) and launch in a daemon thread.
7. **Bot Launch**: Iterate through roles and spawn Discord tasks or Slack threads for each bot with valid tokens.
8. **Signal Management**: Handle `SIGINT`/`SIGTERM` for graceful shutdown.

