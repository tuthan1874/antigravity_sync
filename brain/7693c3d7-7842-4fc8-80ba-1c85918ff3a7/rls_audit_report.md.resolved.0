# Supabase RLS Audit Report — TD Games Platform

**Ngày audit:** 2026-04-24  
**Database:** Supabase project `fifuhkupaqcfjwyouwpa`

---

## Tổng quan

> [!TIP]
> **66/66 bảng đều đã bật RLS** ✅ — Đây là dấu hiệu tốt.

---

## Chi tiết Policies — Bảng nhạy cảm

### 🟢 HR Employees (`hr_employees`)
| Policy | Cmd | Điều kiện |
|---|---|---|
| `hr_admin_hr_full` | ALL | role IN ('admin', 'hr') |
| `hr_employee_read_all` | SELECT | **true** ⚠️ |
| `hr_employee_self_update` | UPDATE | id = user.employee_id |
| `hr_ke_toan_read` | SELECT | role = 'ke_toan' |

> [!WARNING]
> **`hr_employee_read_all`** cho phép **MỌI authenticated user** đọc toàn bộ nhân viên. Nên siết lại thành role-based.

### 🟢 HR Contracts (`hr_contracts`)
| Policy | Cmd | Điều kiện |
|---|---|---|
| `hr_contracts_admin_hr_full` | ALL | role IN ('admin', 'hr') |
| `hr_contracts_ke_toan_read` | SELECT | role = 'ke_toan' |
| `hr_contracts_self_read` | SELECT | employee_id = user.employee_id |

✅ **Tốt** — Phân quyền rõ ràng.

### 🟢 HR Employee Salary (`hr_employee_salary`)
| Policy | Cmd | Điều kiện |
|---|---|---|
| `hr_salary_admin_hr_full` | ALL | role IN ('admin', 'hr') |
| `hr_salary_ke_toan_read` | SELECT | role = 'ke_toan' |

✅ **Tốt** — Chỉ admin/hr/ke_toan xem được lương.

### 🟡 Payroll (`pay_payroll_records`, `pay_payroll_sheets`)
| Policy | Cmd | Điều kiện |
|---|---|---|
| `pay_records_staff` | ALL | `is_staff()` |
| `pay_sheets_staff` | ALL | `is_staff()` |

> [!IMPORTANT]
> Dùng function `is_staff()` — cần verify function này check đúng role. Nên tách READ vs WRITE policy.

### 🔴 CRM Email/Outreach (`crm_email_log`, `crm_outreach_leads`)
| Policy | Cmd | Điều kiện |
|---|---|---|
| `auth_manage_email_log` | ALL | **true** |
| `backend_manage_email_log` | ALL | **true** |
| `auth_manage_outreach` | ALL | **true** |
| `backend_manage_outreach_leads` | ALL | **true** |

> [!CAUTION]
> **ALL policies = `true`** nghĩa là BẤT KỲ authenticated user nào (kể cả member/freelancer) đều có thể đọc/ghi/xóa toàn bộ CRM data! Cần siết lại.

---

## Khuyến nghị

| # | Bảng | Vấn đề | Ưu tiên | Đề xuất |
|---|---|---|---|---|
| 1 | `crm_email_log` | Policy = true | 🔴 Critical | Siết: chỉ admin + ke_toan |
| 2 | `crm_outreach_leads` | Policy = true | 🔴 Critical | Siết: chỉ admin + ke_toan |
| 3 | `hr_employees` | `read_all = true` | 🟡 Medium | Siết: admin + hr + ke_toan + self |
| 4 | Payroll | `is_staff()` chung | 🟡 Medium | Tách read/write policy |
