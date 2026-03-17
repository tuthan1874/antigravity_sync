# Freelancer Contract Generation

## Planning
- [x] Extract text from freelancer PDF templates
- [x] Review HR data model for freelancer fields
- [x] Write implementation plan → approved

## Implementation
- [x] Add `generateHDKV()` to `contractService.ts`
- [x] Add `generateNDA_CTV()` to `contractService.ts`
- [x] Add freelancer types to `CONTRACT_TYPES`
- [x] Update `ContractGenerator.tsx` for employee type detection + project name input
- [x] Update `EmployeeDetail.tsx` button to include freelancer

## Verification
- [x] Test HĐKV preview with freelancer employee
- [x] Test NDA CTV preview
- [x] Test project name updates contract header dynamically
