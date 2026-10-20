---
title: "Trigger - Gmail Unread Conversation Count"
source: https://automagic4android.com/trigger_gmail_unread_conversation_count_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Gmail Unread Conversation Count

The trigger **Gmail Unread Conversation Count** is executed when the count of unread conversations in the Gmail app on the device changes.

Examples:

- Play a notification sound, when more unread conversations are available.

### Settings

#### Accounts

The accounts to check. The sum of unread conversations is checked when multiple accounts are specified.

#### Increasing Unread Count

When checked only executes the trigger when the unread conversation count increases.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `count` — the number of unread conversations
- `old_count` — the number of unread conversations before

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
