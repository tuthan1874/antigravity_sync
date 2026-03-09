# System Audit Fixes — Complete Walkthrough

## Summary

**12/12 items fixed** across P0 (3), P1 (5), P2 (4). **15 files modified**, **2 files created**, **14 unit tests passing**.

---

## P0 Critical Fixes

### active_bots wiring
| File | Change |
|------|--------|
| [discord_bot.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/bots/discord_bot.py) | Self-register on `on_ready()` |
| [slack_bot.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/bots/slack_bot.py) | Self-register during `__init__()` |
| [main.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/main.py) | Pass `active_bots` dict to both bots |

### LLM retry (tenacity)
| File | Change |
|------|--------|
| [llm_utils.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/llm_utils.py) | **[NEW]** Retry decorators + semaphore |
| [intent_detector.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/intent_detector.py) | `@llm_retry_async` on `detect()` |
| [query_engine.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/query_engine.py) | `@llm_retry_sync` on `answer()` + DRY refactor |
| [daily_digest.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/daily_digest.py) | `@llm_retry_sync` on `_summarize_batch()` |
| [scheduled_digest.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/scheduled_digest.py) | `@llm_retry_sync` on `_summarize_messages()` |
| [conversation_manager.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/conversation_manager.py) | `@llm_retry_async` on `parse_date_with_llm()` |

### SQLite thread-safety
`check_same_thread=False` added to all `sqlite3.connect()` calls in: `message_buffer.py`, `conversation_manager.py`, `reminder_manager.py`, `scheduled_digest.py`.

---

## P1 Medium Fixes

### Prompt dedup
- Removed `system_prompt` from all 5 roles in [bot_roles.yaml](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/config/bot_roles.yaml)
- [settings.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/config/settings.py): Default to empty string
- [agent_loader.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/agent_loader.py): Handle empty base prompt gracefully

### Admin auth
- [api.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/admin/api.py): `X-API-Key` header check on all mutating endpoints (POST/PUT/DELETE)
- New setting: `ADMIN_API_KEY` (empty = no auth)

### LLM rate limiting
- [llm_utils.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/llm_utils.py): `asyncio.Semaphore` + `threading.Semaphore`
- [main.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/main.py): `init_llm_semaphores()` at startup
- New setting: `LLM_MAX_CONCURRENT=5`

### Digest run logging
- [daily_digest.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/daily_digest.py): `digest_runs` table with date, role, status, counts, duration, error

### Health check
- [api.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/admin/api.py): `GET /health` → DB, Qdrant, LLM connectivity + bot status

---

## P2 Nice-to-have Fixes

### Team Directory → RAG
- [query_engine.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/query_engine.py): Inject team members list into LLM context
- [main.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/main.py): Pass `team_directory` to QueryEngine

### Auto cleanup — Already existed in [jobs.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/scheduler/jobs.py) (Sunday 4:00 AM)

### Unit tests
- [test_core.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/tests/test_core.py): **[NEW]** 14 tests covering MessageBuffer, ConversationManager, IntentDetector, TeamDirectory

---

## Verification

```
✅ 14/14 unit tests passing
✅ All module imports verified
✅ pytest 9.0.2 + tenacity 9.1.4 installed
```
