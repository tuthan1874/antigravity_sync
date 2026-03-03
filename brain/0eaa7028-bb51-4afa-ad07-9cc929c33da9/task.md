# Refactoring TD Games Invoice Generator

## Planning
- [x] Understand existing NocoDB databases & Tables.
- [x] Draft NocoDB schema (Client, Invoice, Items, BankConfig).
- [x] Design Stitch UI screens (Dashboard, Invoice Editor, History, Settings).
- [x] Prepare Implementation Plan for user approval.

## Execution
- [x] Create NocoDB tables (`v2_Clients`, `v2_Invoices`, `v2_Invoice_Items`, `v2_Bank_Config`).
- [x] Design Stitch UI screens and generate components.
- [x] Create database relationships (Foreign Keys) in NocoDB.
- [x] Connect Stitch UI models & generate components.
- [x] Integrate React frontend with NocoDB API via `services/nocodbService.ts`
- [x] Integrate Stitch UI pages to replace `App.tsx` views.
- [x] Modify `services/outputService` to support PDF/PNG.

## Verification
- [x] Test invoice creation lifecycle (Create, Add Item, Modify Payment details).
- [x] Verify NocoDB record persistence (Save & Load).
- [x] Validate UI theme and responsiveness (Stitch mockups vs components).
- [x] Confirm PDF/PNG/Excel export functionality in the new UI.
- [x] Conduct final bug bash and dependency cleanup.
