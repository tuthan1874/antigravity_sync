# Agent Persona & File-Based Memory (Layer B)

To ensure each bot role has a distinct personality and follows specific operational rules, the system implements an OpenClaw-inspired agent structure. This is the "Layer B" of the memory stack—persistent, file-based context that is read at bot startup and injected into every LLM request.

## Directory Structure
Each agent's persona is defined in a unique directory under `data/agents/{role_id}/`:

```
data/agents/TD_CTO/
├── SOUL.md              # Persona, tone, decision rules
├── IDENTITY.md          # Name, emoji, vibe, identification
├── USER.md              # Human context (Preferences for "Toàn")
├── MEMORY.md            # Persistent standards/decisions
├── TOOLS.md             # Tool-specific config and runbooks
└── memory/              # (Optional) Thematic context chunks
```

## Persona Components
1.  **SOUL.md**: The most critical file. Defines the agent's role (e.g., CTO), Vietnamese/English tone, expertise areas (Architecture, DevOps), and "Safety Rules" (no sharing of API keys).
2.  **IDENTITY.md**: Used for multi-agent disambiguation. Includes display names, emojis (e.g., 🧠 for CTO, 👔 for CEO), and branding colors for the UI.
3.  **USER.md**: Stores information about the main user ("Toàn"). Helps the agent address him correctly and understand his preference for "pragmatic" solutions vs "theoretical" ones.
4.  **MEMORY.md**: Unlike `mem0` (Layer C), this contains *static* or *slow-moving* truths that must be at the forefront (e.g., Tech Stack: Next.js + FastAPI). 
5.  **memory/ Folder**: A place to store larger thematic context (e.g., `company_history.md`, `architecture_standards.md`) as separate files.

## Agent Context Loader
The `core/agent_loader.py` utility handles the extraction of these files:

- **Order of Importance**: It reads and combines files in the order `SOUL -> IDENTITY -> USER -> MEMORY -> TOOLS`.
- **Memory Chunk Loading**: It automatically scans the `memory/` folder for additional `.md` files and appends them.
- **System Prompt Injection**:
    ```python
    def get_system_prompt_with_agent_context(role_id, base_prompt):
        agent_context = load_agent_context(role_id)
        return f"{agent_context}\n\n---\n\n## Additional Instructions\n{base_prompt}"
    ```
- **Priority**: The agent-specific files take precedence over the generic `system_prompt` defined in `bot_roles.yaml`.

## Integration with Query Engine
The `QueryEngine` (`core/query_engine.py`) loads the full agent context on initialization. When answering a user's question, it combines:
1.  The complete **Layer B (Agent Context)**.
2.  Relevant memories retrieved from **Layer C (Qdrant)**.
3.  The user's current **Layer A (Session Context)**.

This ensures the bot's response is consistent with its persona, understands company standards, and remembers previous interactions simultaneously.
