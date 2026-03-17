# Freelancer Contract Generation — Walkthrough

## Changes Made

### 1. `contractService.ts` — 2 New Template Generators

Added `generateHDKV()` (Hợp đồng Khoán việc, 8 sections) and `generateNDA_CTV()` (Thỏa thuận Bảo mật, 17 articles). Content matches original PDFs exactly.

**Key additions:**
- `CONTRACT_TYPES_FULLTIME` / `CONTRACT_TYPES_FREELANCER` arrays for type-based filtering
- `generateHDKV(employee, signingDate, contractNumber, projectName)` — accepts a **project name** for the V/v header
- `generateNDA_CTV(employee, signingDate)` — comprehensive confidentiality agreement

### 2. `ContractGenerator.tsx` — Employee Type Detection

Rewrote to auto-detect employee type and show appropriate contract options:
- **Fulltime** → HĐLĐ, HĐTV, NDA (unchanged)
- **Freelancer** → HĐKV, NDA CTV (new)

Added **project name input** for HĐKV with hint "Mỗi freelancer có thể có nhiều HĐ cho từng dự án". Also added a "Thông tin thù lao" panel showing rate info for freelancers.

### 3. `EmployeeDetail.tsx` — Button Filter

Changed from `employee.type === 'fulltime'` to `(employee.type === 'fulltime' || employee.type === 'freelancer')` with blue gradient for freelancers.

## Verification

### HĐKV with Project Name
![HĐKV contract preview with "Project XYZ" in the V/v header](file:///C:/Users/dangt/.gemini/antigravity/brain/a1cc1332-c952-4a7d-a1ff-e0cb0780b1a4/hdkv_preview_final_project_name_1773758713834.png)

### NDA CTV (17 Articles)
![NDA CTV preview showing Điều 1-2 and detailed confidentiality terms](file:///C:/Users/dangt/.gemini/antigravity/brain/a1cc1332-c952-4a7d-a1ff-e0cb0780b1a4/nda_ctv_preview_top_1773758637296.png)

### Full Flow Recording
![Browser recording of testing the freelancer contract flow](file:///C:/Users/dangt/.gemini/antigravity/brain/a1cc1332-c952-4a7d-a1ff-e0cb0780b1a4/freelancer_contract_test_1773758518795.webp)

## Result
✅ All contracts render correctly with employee data populated, project name is dynamic, and A4 layout is optimized.
