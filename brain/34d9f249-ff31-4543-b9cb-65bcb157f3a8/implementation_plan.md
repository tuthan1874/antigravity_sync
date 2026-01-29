# Implementation Plan: Missing Features

## Goal
Implement the remaining features identified in the project audit to complete the Task Management application according to `plan.md`.

---

## Audit Summary

| Feature | DB Table | RLS | Frontend CRUD | Status |
|---------|----------|-----|---------------|--------|
| Profiles | ✅ | ✅ | ✅ | **Complete** |
| Workspaces | ✅ | ✅ | ✅ | **Complete** |
| Members | ✅ | ✅ | ✅ | **Complete** |
| Tasks | ✅ | ✅ | ✅ | **Complete** |
| Tags | ✅ | ✅ | ❌ (Read-only) | **Needs CRUD** |
| Task_Tags | ✅ | ✅ | ❌ | **Needs UI** |
| Comments | ✅ | ✅ | ❌ (Placeholder) | **Needs Implementation** |
| Checklists | ✅ | ✅ | ❌ (Read-only) | **Needs CRUD** |
| Attachments | ✅ | ✅ | ✅ | **Complete** |
| Activity_Logs | ✅ | ✅ | ✅ | **Complete** |
| n8n Workflows | ✅ | N/A | N/A | **Complete** |

---

## Proposed Changes

### 1. Comments Feature (Priority: High)

#### [NEW] [useComments.ts](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/hooks/useComments.ts)
- Create hook with `useComments(taskId)` query
- Add `useCommentMutations()` for create/update/delete
- Follow existing patterns from `useTasks.ts`

#### [NEW] [CommentsSection.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/CommentsSection.tsx)
- Comment list with rich text display (TipTap)
- Add comment form with rich text editor
- Edit/delete capabilities for own comments

#### [MODIFY] [TaskDetailPage.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/TaskDetailPage.tsx)
- Replace "Comments feature coming soon..." placeholder with `<CommentsSection />`

---

### 2. Checklists CRUD Feature (Priority: Medium)

#### [NEW] [useChecklists.ts](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/hooks/useChecklists.ts)
- `useChecklists(taskId)` query
- `useChecklistMutations()` for add/toggle/delete/reorder items

#### [NEW] [ChecklistSection.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/ChecklistSection.tsx)
- Interactive checklist with add item input
- Toggle checkbox functionality
- Delete item capability
- Drag-and-drop reordering (optional)

#### [MODIFY] [TaskDetailPage.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/TaskDetailPage.tsx)
- Replace static checklist display with interactive `<ChecklistSection />`

---

### 3. Tags CRUD Feature (Priority: Medium)

#### [NEW] [useTags.ts](file:///e:/TDC_App/Task%20Management/web/src/features/workspaces/hooks/useTags.ts)
- `useTags(workspaceId)` query for workspace tags
- `useTagMutations()` for create/update/delete tags
- `useTaskTagMutations(taskId)` for add/remove tags from tasks

#### [NEW] [TagsManager.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/workspaces/components/TagsManager.tsx)
- Workspace-level tag management UI
- Create new tags with color picker
- Edit/delete existing tags

#### [NEW] [TaskTagsSelector.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/TaskTagsSelector.tsx)
- Multi-select dropdown for assigning tags to tasks
- Shows available workspace tags
- Allows adding/removing tags from task

#### [MODIFY] [TaskDetailPage.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/TaskDetailPage.tsx)
- Replace static tags display with interactive `<TaskTagsSelector />`

#### [MODIFY] [TaskForm.tsx](file:///e:/TDC_App/Task%20Management/web/src/features/tasks/components/TaskForm.tsx)
- Add tag selection to task creation/edit form

---

## Files NOT Changed (Already Complete)
- All Supabase migrations (DB schema complete)
- All RLS policies (security complete)
- `useFileUpload.ts` and `upload-file` edge function (attachments complete)
- `useTaskRealtime.ts` (realtime complete)
- n8n workflows (automation complete)

---

## Verification Plan

### Manual Testing
Since there are no existing frontend tests discovered, verification will be manual:

1. **Comments Feature Test**
   - Navigate to any task detail page
   - Add a new comment using the rich text editor
   - Verify comment appears in the list
   - Edit the comment, verify changes saved
   - Delete the comment, verify removal

2. **Checklists Feature Test**
   - Open a task detail page
   - Add a new checklist item
   - Toggle the checkbox, verify `is_done` updates
   - Delete the item, verify removal
   - Verify progress counter updates correctly

3. **Tags Feature Test**
   - Go to workspace settings or tags manager
   - Create a new tag with custom color
   - Open a task, add the tag
   - Verify tag appears on task
   - Remove tag from task
   - Delete the tag from workspace

### Browser Verification
After implementation, run the dev server:
```bash
cd e:\TDC_App\Task Management\web
npm run dev
```
Then navigate to `http://localhost:3000` and test each feature.

---

## User Review Required

> [!IMPORTANT]
> Please confirm if you want me to proceed with implementing all three features (Comments, Checklists CRUD, Tags CRUD) in the order listed above. 
> 
> Alternatively, let me know if you'd like to prioritize specific features or skip any that aren't needed.

