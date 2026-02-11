# Phase 2: Project Cleanup & Continued Optimization

## Part A: Database
- [x] A1. Optimize ~35 RLS policies — wrap `auth.uid()` in `(select ...)`
- [x] A2. Add RLS policies for 4 tables without policies

## Part B: Project Cleanup
- [x] B1. Delete unused/orphaned files (11 files)
- [x] B2. Consolidate root .md docs → `docs/`
- [x] B3. Archive database scripts → `database/archive/`
- [x] B4. Delete test/demo routes and data files
- [x] B5. Split `lib/services.ts` → domain-specific modules

## Verification
- [x] Run `npm run build` ✅ (exit code 0)
