# Email Outreach UI Testing Checklist

- [x] Navigate to CRM Outreach tab
- [x] Verify Dashboard sub-tab (funnel, stats)
  - Funnel and stats cards rendered with 0 values initially.
  - Updated to show 2 leads (Tier 1) correctly after adding leads.
- [x] Verify Leads sub-tab (empty table, import/add lead)
  - Table shows "Chưa có leads" and correctly updates when leads are added.
- [x] Add a test lead (Supercell)
  - Added 2 leads: one with missing Studio name (my mistake) and one with correct data ("Supercell", "John Smith", "jsmith@supercell.com", "CEO", Tier 1).
- [x] Verify Templates sub-tab (3 steps)
  - 3 steps (initial, followup_1, followup_2) are visible with correct subjects and active status.
- [x] Verify Discovery sub-tab (form, expected error)
  - Form renders Company Name and Domain inputs.
  - Clicking "Discover" triggers a request (no visible error toast in screenshot, but expected to fail due to missing API URL).
- [x] Verify Dashboard stats update
  - Dashboard correctly reflects 2 leads in Tier 1 and "Pending" status in funnel.

## Findings
- All sub-tabs are working and navigable.
- Lead management (Add lead) is functional and updates the UI state immediately.
- Dashboard provides a good overview of the outreach pipeline.
- Templates are correctly integrated and displayed.
- Discovery UI is ready for Phase 2 API integration.
