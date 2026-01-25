# Project Walkthrough

## Project Setup

The `hiring_app` is a **Vite + React + TypeScript** job application portal for TD Games.

### Setup Steps
1.  **Dependencies**: Installed via `npm install`
2.  **Dev Server**: Started via `npm run dev`
3.  **Local URL**: [http://localhost:8080/](http://localhost:8080/)

![Home Page](file:///C:/Users/dangt/.gemini/antigravity/brain/bf54cc8d-f147-4d4e-92b3-237f61b3cc79/hiring_app_home_1769161798620.png)

---

## Security Audit

> [!WARNING]
> Found **exposed API credentials** hardcoded in frontend code!

### Sensitive Data Found

| File | Issue |
|------|-------|
| [useJobs.ts](file:///e:/TDC_App/TDGAMES_App/hiring_app/src/hooks/useJobs.ts) | NocoDB URL, Table ID, **API Token (xc-token)** |
| [ApplicationForm.tsx](file:///e:/TDC_App/TDGAMES_App/hiring_app/src/components/ApplicationForm.tsx) | n8n Webhook URL |

### Changes Made

1.  **Created [.env](file:///e:/TDC_App/TDGAMES_App/hiring_app/.env)** with all sensitive values
2.  **Updated source files** to use `import.meta.env.VITE_*` variables
3.  **Created [.env.example](file:///e:/TDC_App/TDGAMES_App/hiring_app/.env.example)** as template (no secrets)
4.  **Updated [.gitignore](file:///e:/TDC_App/TDGAMES_App/hiring_app/.gitignore)** to exclude `.env`

### Diff Summary

```diff
# useJobs.ts
-const NOCODB_URL = "https://nocodb.tdconsulting.vn";
-const API_TOKEN = "crlf2AYH...X7Tp";
+const NOCODB_URL = import.meta.env.VITE_NOCODB_URL || "...";
+const API_TOKEN = import.meta.env.VITE_NOCODB_API_TOKEN || "";

# ApplicationForm.tsx
-await fetch("https://n8n.tdconsulting.vn/webhook/tdgames-apply", ...)
+await fetch(import.meta.env.VITE_WEBHOOK_URL || "...", ...)
```
