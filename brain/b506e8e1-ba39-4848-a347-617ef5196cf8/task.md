# Migration: NocoDB → Supabase

## Phase 1: Supabase Schema
- [ ] Create `invoice_studios` table
- [ ] Create `invoice_banks` table
- [ ] Create `invoice_clients` table
- [ ] Create `invoice_invoices` table
- [ ] Create `invoice_accounts` table
- [ ] Enable RLS on all tables

## Phase 2: Data Migration
- [ ] Migrate studios data
- [ ] Migrate banks data
- [ ] Migrate clients data
- [ ] Migrate invoices data
- [ ] Migrate accounts data
- [ ] Verify row counts

## Phase 3: Service Layer Rewrite
- [ ] Create `supabaseClient.ts`
- [ ] Create `supabaseService.ts` (drop-in replacement)
- [ ] Update `App.tsx` imports
- [ ] Update `LoginScreen.tsx`
- [ ] Update `.env.local`

## Phase 4: Cleanup
- [ ] Remove NocoDB env vars
- [ ] Delete `nocodbService.ts`
- [ ] Verify TypeScript compilation
- [ ] Test all features in browser
