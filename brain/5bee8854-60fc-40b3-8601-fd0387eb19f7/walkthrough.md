# TD GAMES Platform — Folder Restructure Walkthrough

## What Was Done

Restructured the TD GAMES app from a single-app architecture to a **multi-app platform** with an iPhone-style App Launcher.

### Architecture Changes

```
Before:                          After:
├── App.tsx (monolith)           ├── App.tsx (platform shell)
├── components/ (all mixed)      ├── components/ (shared only)
├── hooks/                       │   ├── LoginScreen.tsx
├── services/                    │   ├── HomeScreen.tsx ← NEW
│   ├── supabaseClient.ts       │   ├── Button.tsx
│   ├── supabaseService.ts      │   ├── FormElements.tsx
│   ├── exportService.ts        │   └── ToastNotification.tsx
│   ├── sePayService.ts         ├── config/
│   └── exchangeRateService.ts  │   └── apps.ts ← NEW (app registry)
└── constants.ts                ├── services/ (shared)
                                │   └── supabaseClient.ts
                                ├── apps/
                                │   └── invoice/
                                │       ├── components/ (10 files)
                                │       │   ├── InvoiceApp.tsx ← NEW
                                │       │   ├── Navbar.tsx (+ back button)
                                │       │   ├── InvoiceEditor.tsx
                                │       │   └── ... (7 more)
                                │       ├── hooks/
                                │       │   └── useInvoiceState.ts
                                │       └── services/
                                │           ├── supabaseService.ts
                                │           ├── exportService.ts
                                │           ├── sePayService.ts
                                │           └── exchangeRateService.ts
                                ├── constants.ts
                                └── types.ts
```

### Key New Files

| File | Purpose |
|------|---------|
| `config/apps.ts` | App registry — add new apps by adding entries here |
| `components/HomeScreen.tsx` | iPhone-style launcher with animated app cards |
| `apps/invoice/components/InvoiceApp.tsx` | Self-contained Invoice module wrapper |

### Import Strategy
- **Root-level imports**: Use `@/` alias (e.g., `@/types`, `@/components/Button`)
- **Intra-module imports**: Use relative paths (e.g., `../services/supabaseService`)

## Verification

### TypeScript Build
`npx tsc --noEmit` — **0 errors** ✅

### Browser Testing

````carousel
![Home Screen — App Launcher with Invoice and Expense cards](C:\Users\dangt\.gemini\antigravity\brain\5bee8854-60fc-40b3-8601-fd0387eb19f7\home_screen_1773508183835.png)
<!-- slide -->
![Invoice App — with back button in navbar](C:\Users\dangt\.gemini\antigravity\brain\5bee8854-60fc-40b3-8601-fd0387eb19f7\invoice_app_1773508194301.png)
````

### Flow Verified ✅
1. Login → Home Screen → shows Invoice & Expense cards
2. Click Invoice → loads full Invoice app with ← back button
3. Click ← back → returns to Home Screen
4. Expense card → shows "Đang phát triển..." placeholder
