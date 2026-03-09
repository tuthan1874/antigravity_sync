# Fix P0 Critical Issues

## P0-1: Fix `active_bots` population
- [ ] Register Discord bot instances into `active_bots` dict on `on_ready()`
- [ ] Register Slack bot instances into `active_bots` dict on start
- [ ] Pass `active_bots` ref to bot constructors
- [ ] Verify `digest_send_callback` can find bots

## P0-2: Add LLM retry + error handling
- [ ] Add `tenacity` to `requirements.txt`
- [ ] Wrap LLM calls in `IntentDetector.detect()` with retry
- [ ] Wrap LLM calls in `QueryEngine.answer()` / `answer_sync()` with retry
- [ ] Wrap LLM calls in `DailyDigest._summarize_batch()` with retry
- [ ] Wrap LLM calls in `ScheduledDigest._summarize_messages()` with retry
- [ ] Wrap LLM calls in `ConversationManager.parse_date_with_llm()` with retry

## P0-3: Fix SQLite thread-safety
- [ ] Update `MessageBuffer` to use thread-safe connection pattern
- [ ] Update `ConversationManager` to use thread-safe connection pattern
- [ ] Update `ReminderManager` to use thread-safe connection pattern
- [ ] Update `ScheduledDigestManager` to use thread-safe connection pattern

## P1 Quick Win: Refactor `query_engine.py` DRY
- [ ] Eliminate `answer_sync()` duplication
