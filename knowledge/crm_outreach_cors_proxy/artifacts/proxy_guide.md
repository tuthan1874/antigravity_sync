# CRM Email Outreach - CORS Proxy & Auto Batch

## Problem
Frontend at `localhost:3001` calling VPS API at `https://app.tdgamestudio.com/outreach-api` was blocked by CORS. All buttons (Verify Emails, Check Bounces, Gửi Batch, Discovery) failed silently.

## Solution: Supabase Edge Function Proxy

### Architecture
```
Frontend → Supabase Edge Function (outreach-proxy) → VPS FastAPI (180.93.144.98:8401)
```

### Key Code
```typescript
// EmailOutreach.tsx
function getOutreachAPI(): string {
  const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
  if (supabaseUrl) return `${supabaseUrl}/functions/v1/outreach-proxy`;
  return import.meta.env.VITE_OUTREACH_API_URL || '';
}
```

### Edge Functions
| Function | Purpose |
|----------|---------|
| `outreach-proxy` | CORS proxy, forwards all requests to VPS API |
| `outreach-auto-batch` | Auto daily email sender, reads config from DB |

### Auto Batch Config
- **Table**: `crm_outreach_config` (key='auto_batch')
- **Fields**: enabled, batch_size (15), daily_limit (30), min_delay_hours (72)
- **Schedule**: pg_cron at 00:00 UTC (7AM VN) + 07:00 UTC (2PM VN)
- **Log**: `crm_outreach_batch_log` table

### Batch Logic
1. Send initial emails to pending leads (Tier 1 first)
2. Send follow-ups to eligible leads (72h after previous)
3. Respect daily quota from VPS API
4. Log results to crm_outreach_batch_log

### Environment
- **VPS API**: `OUTREACH_VPS_API` env var on Edge Function (default: `http://180.93.144.98:8401`)
- **Sender**: toan.dang@tdgamestudio.com via Gmail API
