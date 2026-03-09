# Fix P0 Critical Issues

## P0-1: Fix `active_bots` population
- [x] Register Discord bot instances into `active_bots` dict on `on_ready()`
- [x] Register Slack bot instances into `active_bots` dict on start
- [x] Pass `active_bots` ref to bot constructors via `run_discord_bot` / `run_slack_bot`
- [x] Wire `active_bots` from `main.py` into both bot launchers

## P0-2: Add LLM retry + error handling
- [x] Create `core/llm_utils.py` with tenacity retry decorators
- [x] Add `tenacity>=8.0` to `requirements.txt`
- [x] Wrap LLM calls in `IntentDetector.detect()` with retry
- [x] Wrap LLM calls in `QueryEngine.answer()` with retry
- [x] Wrap LLM calls in `DailyDigest._summarize_batch()` with retry
- [x] Wrap LLM calls in `ScheduledDigest._summarize_messages()` with retry
- [x] Wrap LLM calls in `ConversationManager.parse_date_with_llm()` with retry

## P0-3: Fix SQLite thread-safety
- [x] `MessageBuffer` — `check_same_thread=False`
- [x] `ConversationManager` — `check_same_thread=False`
- [x] `ReminderManager` — `check_same_thread=False`
- [x] `ScheduledDigestManager` — `check_same_thread=False`

## P1 Quick Win: Refactor `query_engine.py` DRY
- [x] Eliminate `answer_sync()` duplication (~60 lines removed)
