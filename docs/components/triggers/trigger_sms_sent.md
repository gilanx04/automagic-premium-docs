---
title: "Trigger - SMS Sent"
source: https://automagic4android.com/trigger_sms_sent_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - SMS Sent

The trigger **SMS Sent** is executed when an SMS is sent and stored as a sent SMS in the default SMS outbox of the standard Android SMS database.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Send every sent SMS as a mail to your mail account.

### Settings

#### SMS Receiver List

The list of call numbers when the flow is executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

#### Contains Text

Only executes the flow when the text of the SMS contains the given text (no wildcards supported). The text is not case sensitive.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `sms_text` — the text of the SMS
- `sms_receiver` — the receiver of the SMS
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
