# AI Excel Generator — MVP Walkthrough

## Tổng quan

Đã hoàn thành **Phase 1 MVP** — ứng dụng web tạo file Excel chuyên nghiệp bằng AI.

## Kiến trúc

| Service | Tech | Port | Status |
|---|---|---|---|
| **Frontend + AI** | Next.js 16 + TypeScript | 3000 | ✅ Build OK |
| **Excel Engine** | FastAPI + openpyxl | 8000 | ✅ Running |

## Files đã tạo

### Python Engine (`engine/`)
- [themes.py](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/engine/themes.py) — 5 color themes (Corporate Blue, Maroon, Teal, Dark Mode, Forest Green)
- [excel_from_json.py](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/engine/excel_from_json.py) — JSON → Excel converter (groups, merge, multi-sheet)
- [server.py](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/engine/server.py) — FastAPI server (`/export-excel`, `/themes`, `/health`)

### AI Integration (`app/src/lib/`)
- [aiProvider.ts](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/app/src/lib/aiProvider.ts) — OpenRouter client (Claude, Gemini, GPT-4o)
- [system-prompt.ts](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/app/src/lib/prompts/system-prompt.ts) — AI system prompt + template chips

### Frontend (`app/src/app/`)
- [page.tsx](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/app/src/app/page.tsx) — Main UI (chat, preview, export, settings modal)
- [globals.css](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/app/src/app/globals.css) — Dark glassmorphism design
- [route.ts](file:///e:/TDC_App/TDGAMES_App/excel-professional-skill/app/src/app/api/generate/route.ts) — `/api/generate` endpoint

## Cách sử dụng

### 1. Start Python Engine
```bash
cd engine
python server.py
# → Running on http://0.0.0.0:8000
```

### 2. Start Next.js Frontend
```bash
cd app
npm run dev
# → http://localhost:3000
```

### 3. Mở app → Settings → Nhập OpenRouter API key

### 4. Nhập prompt hoặc click template chip → AI tạo JSON → Preview → Download Excel

## Verification Results

| Test | Result |
|---|---|
| `npm run build` | ✅ Compiled successfully |
| `/health` | ✅ `{"status":"ok"}` |
| `/themes` | ✅ 5 themes returned |
| `/export-excel` (POST JSON) | ✅ .xlsx file generated |
| Python engine standalone | ✅ `demo_output.xlsx` created |

## Next Steps
- Nhập OpenRouter API key để test full E2E (prompt → AI → preview → download)
- Phase 2: Google Sheets integration
