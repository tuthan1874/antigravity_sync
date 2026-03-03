# Technical Specification: TD Games Invoice Generator V2

This document provides a comprehensive overview of the architecture, database schema, and design principles used in the TD Games Invoice Generator V2. You can use this as a blueprint for creating similar enterprise-grade billing applications.

## 1. Technology Stack
- **Frontend Framework:** React 18+ with Vite (for fast development and bundling).
- **Backend (Database):** NocoDB (No-code database providing a REST API layer).
- **API Communication:** Axios (handling structured requests with Bearer Token auth).
- **Styling:** Modern Vanilla CSS (using CSS Variables, Glassmorphism, and Flex/Grid layouts).
- **Export Engines:** 
    - `html2canvas` (UI to Image)
    - `jspdf` (Image/HTML to PDF)
    - `xlsx` (JSON to Excel)

## 2. Database Schema (NocoDB)

### Table: `v2_Invoice_Clients`
| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | Primary Key | Unique ID |
| `Name` | SingleLineText | Client's full name/Company name |
| `Email` | Email | Contact email for billing |
| `Address` | LongText | Billing address |
| `TaxId` | SingleLineText | Client's tax identification number |

### Table: `v2_Invoices`
| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | Primary Key | Unique ID |
| `InvoiceNumber` | SingleLineText | Display ID (e.g., INV-2024-001) |
| `Date` | Date | Issue date |
| `Status` | SingleSelect | Paid, Pending, Overdue, Draft |
| `Currency` | SingleSelect | USD, VND, EUR |
| `TaxRate` | Percent | Global tax percentage (0 to 1) |
| `TotalAmount` | Decimal | Calculated total (stored for quick list view) |
| `fk_ClientId` | LinkToAnother | Relationship to `v2_Invoice_Clients` |

### Table: `v2_Invoice_Items`
| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | Primary Key | Unique ID |
| `Description` | LongText | Description of work/product |
| `Quantity` | Number | Quantity of items |
| `UnitPrice` | Decimal | Price per unit |
| `fk_InvoiceId` | LinkToAnother | Relationship to `v2_Invoices` |

### Table: `v2_Bank_Profiles`
| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | Primary Key | Unique ID |
| `BankName` | SingleLineText | Bank Name |
| `AccountName` | SingleLineText | Owner Name |
| `AccountNumber` | SingleLineText | Account Number |
| `SWIFT` | SingleLineText | Swift/BIC code (optional) |

## 3. Core Architecture
- **Service-Oriented Design:** All database logic is decoupled into `services/nocodbService.ts`. This allows you to swap NocoDB for Supabase or a custom API without touching the UI components.
- **View Management:** A simple state-based router in `App.tsx` handles switching between the **Dashboard** and **Editor**.
- **Live Preview Pattern:** The Editor component maintains a local `InvoiceData` object. Every input change triggers a re-render of a specialized `InvoicePreview` component, ensuring "What You See Is What You Get."

## 4. UI/UX Design System
- **Theme:** Ultra-dark mode (`#0f1218` background).
- **Accents:** Neon green (`#2bee79`) for "Create/Save" actions, Gold (`#f1c40f`) for critical alerts.
- **Visual Effects:** 
    - `backdrop-filter: blur(10px)` for glassmorphism panels.
    - Subtle gradients for header text.
    - Consistent `border-radius: 12px` for modern card layouts.
- **Typography:** Inter or Roboto (Google Fonts) for a clean, professional look.

## 5. Integration Workflow
1. **Initialize Project:** `npm create vite@latest` (React + TS).
2. **Setup Backend:** Create tables in NocoDB and get the API Token.
3. **Environment Config:** Store base URL and tokens in `.env.local`.
4. **Develop Service Layer:** Implement CRUD functions using Axios.
5. **UI Development:** Build the Dashboard and Editor using the established design tokens.
6. **Export Logic:** Add listeners for the export buttons to trigger `html2canvas` and `jspdf`.
