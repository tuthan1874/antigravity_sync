# Agent Folder Structure & Memory Layers (Implemented)

Based on the [OpenClaw](https://github.com/nextlevelbuilder/openclaw) agent model, the system uses a structured organization for bot personas and persistent context across all roles.

## 1. Directory Structure

Each bot role (agent) has its own configuration directory within `data/agents/{role_id}/`:

| File | Purpose |
|------|---------|
| `SOUL.md` | **Persona / Rules**: The agent's tone, decision-making principles, and safety rules. The core identity. |
| `IDENTITY.md` | **Identification**: Display name, role description, vibe, and representative emoji. |
| `USER.md` | **Human Context**: Preferences for the specific user (e.g., Toan), including timezone and address style. |
| `MEMORY.md` | **Fixed Memory (Layer B)**: Durable business context, standards, and historical decisions in Markdown format. |
| `memory/*.md` | **Memory Chunks**: Subject-specific context (e.g., `tech_standards.md`) that is too large for `MEMORY.md`. |
| `TOOLS.md` | **Tool Config**: Specific endpoints and instructions for tools used by that agent (ClickUp, Qdrant). |

## 2. Three-Layer Memory Model

The bots utilize three distinct layers of memory to provide accurate and context-aware responses:

### Layer A: Session Context (Short-Term)
- **What**: Conversation history in the current chat session/thread.
- **Persistence**: Temporary, limited by the model's context window.
- **Usage**: Handles follow-up questions and immediate thread context.

### Layer B: Workspace Memory (Medium-Term / File-Based)
- **What**: Content from `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`, and `memory/*.md` in the agent's folder.
- **Persistence**: Durable and easily editable by humans.
- **Usage**: Injected into the **System Prompt** every single time. This ensures the bot never "forgets" foundational company rules, its own persona, or user preferences.

### Layer C: Long-Term Memory (Persistent / Vector Search)
- **What**: Mem0-managed storage in **Qdrant**.
- **Persistence**: Indefinite. Collections are scoped to each bot role.
- **Usage**: RAG (Retrieval-Augmented Generation). The agent searches for relevant facts from past chat history or summarized digests when the user asks a question.

## 3. Benefits of this Architecture
- **Isolation**: Each bot has its own "brain" folder, making it easy to clone or customize roles without touching the codebase.
- **Persona Depth**: Detailed `SOUL.md` files allow for much richer character interaction compared to single-line prompts.
- **Contextual Integrity**: Layer B ensures the bot always operates within company standards and project history, regardless of whether a semantic search (Layer C) finds a match.
- **Maintainability**: Using Markdown files makes it trivial to update bot knowledge or user preferences using standard text editors.
