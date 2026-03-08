# Async Implementation Patterns

## 1. Sync-to-Async Bridge (Slack Bolt)
Slack Bolt handlers are synchronous by design. To execute async ClickUp calls or LLM queries from within these handlers, a bridge is used to run the coroutine in the event loop.

```python
def _run_async(coro):
    """Run an async coroutine from a sync Slack Bolt handler."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(asyncio.run, coro)
                return future.result(timeout=120)
        else:
            return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)
```

## 2. Background Task Threads
The Admin UI (FastAPI/Uvicorn) and Slack bots are run in separate `threading.Thread` instances with `daemon=True`. This allows them to coexist with the main `asyncio` event loop running the Discord bots.

```python
def run_admin_server():
    import uvicorn
    uvicorn.run(admin_app, host="0.0.0.0", port=8500, log_level="warning")

admin_thread = threading.Thread(target=run_admin_server, daemon=True)
admin_thread.start()
```
