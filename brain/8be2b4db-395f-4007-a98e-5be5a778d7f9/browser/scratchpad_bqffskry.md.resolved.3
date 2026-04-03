# Task: Investigate Blank Page at http://localhost:5173/

## Checklist
- [x] Read current browser state (logs, network, DOM)
- [x] Identify the cause of the blank page (Missing export 'SpineViewerHandle' in SpineViewer.tsx)
- [ ] Fix the issue if it's code-related (Requires parent agent to edit files)
- [ ] Verify the fix by reloading and checking the UI

## Observations
- User reported "Trắng trơn chả có gì" (completely blank).
- App uses React + Vite + TailwindCSS 4 + Supabase.
- Manual import test revealed: `SyntaxError: The requested module '/src/components/viewer/SpineViewer.tsx' does not provide an export named 'SpineViewerHandle'`.
- `ViewerPage.tsx` imports `SpineViewerHandle`, but `SpineViewer.tsx` does not export it (or it's only a type and needs to be used with `import type`).
- Because of this module resolution error, `main.tsx` fails to initialize, leaving the root empty and the console without standard React errors.
- The mysterious "Subagent check" logs are likely system-injected or leftovers and not the primary cause.
