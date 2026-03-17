# Freelancer Contract Generation

## Planning
- [x] Extract text from freelancer PDF templates
- [x] Review HR data model for freelancer fields
- [x] Write implementation plan → approved

## Implementation
- [ ] Add `generateHDKV()` to `contractService.ts`
- [ ] Add `generateNDA_CTV()` to `contractService.ts`
- [ ] Add freelancer types to `CONTRACT_TYPES`
- [ ] Update `ContractGenerator.tsx` for employee type detection + project name input
- [ ] Update `EmployeeDetail.tsx` button to include freelancer

## Verification
- [ ] Test HĐKV preview with freelancer employee
- [ ] Test NDA CTV preview
- [ ] Verify print/export works
