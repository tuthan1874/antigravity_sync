# Người phụ thuộc (Dependents) — HR Module

Thêm quản lý người phụ thuộc cho nhân viên fulltime — phục vụ tính giảm trừ gia cảnh (4.4tr/tháng/người) khi tính thuế TNCN.

## Proposed Changes

### Database

#### [NEW] Migration: `hr_dependents` table

```sql
CREATE TABLE hr_dependents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  employee_id UUID NOT NULL REFERENCES hr_employees(id) ON DELETE CASCADE,
  full_name TEXT NOT NULL,
  relationship TEXT NOT NULL,        -- 'parent' | 'child' | 'spouse' | 'other'
  date_of_birth DATE,
  id_number TEXT,                    -- CCCD/CMND
  tax_code TEXT,                     -- MST người phụ thuộc (nếu có)
  deduction_from DATE,               -- Ngày bắt đầu giảm trừ
  deduction_to DATE,                 -- Ngày kết thúc
  status TEXT DEFAULT 'active',      -- 'active' | 'inactive'
  notes TEXT DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE hr_dependent_documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dependent_id UUID NOT NULL REFERENCES hr_dependents(id) ON DELETE CASCADE,
  doc_type TEXT NOT NULL,            -- 'cccd' | 'birth_cert' | 'residence' | 'student_card' | 'disability_cert' | 'adoption' | 'income_cert' | 'other'
  file_url TEXT NOT NULL,
  file_name TEXT DEFAULT '',
  notes TEXT DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT now()
);
```

RLS: `FOR ALL USING (true)` (consistent with existing tables).

> [!NOTE]
> Mỗi người phụ thuộc có thể có nhiều giấy tờ đính kèm (CCCD, giấy khai sinh, thẻ SV, v.v.)

---

### TypeScript Types

#### [MODIFY] [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts)

Add `HrDependent` and `HrDependentDocument` interfaces.

---

### Service Layer

#### [MODIFY] [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts)

Add CRUD functions:
- `fetchDependents(employeeId)` — with joined documents
- `saveDependent(data)` / `updateDependent(id, updates)` / `deleteDependent(id)`
- `saveDependentDocument(data)` / `deleteDependentDocument(id)`

---

### UI Components

#### [MODIFY] [EmployeeForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeForm.tsx)

Add section **"👨‍👩‍👧‍👦 Người phụ thuộc"** (fulltime only, after salary section):
- List existing dependents as expandable cards
- Each card shows: name, relationship, DOB, ID number, status
- Expand → shows document list with upload button
- Button to add new dependent (inline form)
- Documents: upload to R2 using existing `uploadFileToR2`

Document types dropdown:
| Code | Label |
|---|---|
| `cccd` | CMND/CCCD |
| `birth_cert` | Giấy khai sinh |
| `residence` | Giấy xác nhận cư trú |
| `student_card` | Thẻ sinh viên |
| `disability_cert` | Giấy xác nhận khuyết tật |
| `adoption` | Quyết định nhận nuôi |
| `income_cert` | Xác nhận thu nhập |
| `other` | Khác |

---

## Verification Plan

### Browser Testing
- Navigate to employee form → verify "Người phụ thuộc" section appears for fulltime
- Add a dependent with documents → verify save to DB
- Edit/delete dependent → verify CRUD works
- Verify document upload to R2 works
