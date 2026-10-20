---
title: "Trigger - SMS Received"
source: https://automagic4android.com/trigger_sms_receive_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - SMS Received

The trigger **SMS Received** is executed when an SMS is received depending on the criteria defined in the options.

Examples:

- Play a special alert when an SMS contains the keyword **Alert!**
- Send an SMS containing your location back to the SMS sender when the SMS contains **Where are you?**
- Read the received SMS aloud.
- Delete a password file on the SD card when the SMS contains **house search!**
- Play a repeating sound and vibrate when an SMS contains **device lost!**

Tip: Use a keyword or password that will not be part of a regular SMS to avoid unpleasant surprises.

### Settings

#### SMS Sender List

The list of call numbers when the flow is executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter out similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

Warning: The formatting of the incoming number depends on the operator in use.
You have to check the log file to see the exact formatting used or you can add an action **Notification on Screen** with text `{sms_sender}` to see the actual number.

#### Contains Text

Only executes the flow when the text of the SMS contains the given text (no wildcards supported). The text is not case sensitive.

#### Prevent other apps from receiving the SMS

Prevents the default SMS application from receiving the SMS.

Warning: You may end up overlooking SMS you didn't intend to be matched (due to not having appeared in your messaging app).
Warning: This feature is not supported on Android 4.4+.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `sms_text` — the text of the SMS
- `sms_sender` — the sender of the SMS
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
