# Fix Attachment Syncing Bugs

## Bug 1: Discord Source Duplication
- [ ] Investigate `src/webhooks/discord.js` handling of incoming attachments.
- [ ] Investigate why Discord echoes attachments (2x on Discord).
- [ ] Investigate why Slack receives 2x text and 2x attachments when Discord syncs.

## Bug 2: Slack Source Attachment to ClickUp
- [ ] Investigate `src/webhooks/slack.js` handling of incoming attachments.
- [ ] Investigate `src/relay.js` and ClickUp API logic to see why attachments from Slack are not sent to ClickUp.
- [ ] Implement file upload to ClickUp task/comment from Slack attachment.

## Verification
- [ ] Test Discord to Slack/ClickUp with attachments.
- [ ] Test Slack to Discord/ClickUp with attachments.
