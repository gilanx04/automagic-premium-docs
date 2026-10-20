---
title: "Condition - Gmail Unread Conversation Count"
source: https://automagic4android.com/condition_gmail_unread_conversation_count_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Gmail Unread Conversation Count

The condition **Gmail Unread Conversation Count** checks the number of unread conversations available in the Gmail app on the device.

Examples:

- Play an alert sound every 5 minutes when unread conversations are available.

### Settings

#### Condition

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported count is below the defined count

**higher than**
true when the reported count is above the defined count

**exactly**
true when the reported count is exactly matches the defined count

#### Unread Count

The number to compare in the condition.

#### Accounts

The accounts to check. The sum of unread conversations is checked when multiple accounts are specified. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `count` — the number of unread conversations

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
