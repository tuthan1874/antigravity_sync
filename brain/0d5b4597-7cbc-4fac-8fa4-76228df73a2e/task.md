# Fix Attachment Syncing Bugs

## Bug 1: Discord Source Duplication
- [x] Investigate `src/webhooks/discord.js` handling of incoming attachments.
- [x] Investigate why Discord echoes attachments (2x on Discord).
- [x] Investigate why Slack receives 2x text and 2x attachments when Discord syncs.

## Bug 2: Slack Source Attachment to ClickUp
- [x] Investigate `src/webhooks/slack.js` handling of incoming attachments.
- [x] Investigate `src/relay.js` and ClickUp API logic to see why attachments from Slack are not sent to ClickUp.
- [x] Implement file upload to ClickUp task/comment from Slack attachment.

## Verification
- [ ] Test Discord to Slack/ClickUp with attachments.
- [ ] Test Slack to Discord/ClickUp with attachments.
