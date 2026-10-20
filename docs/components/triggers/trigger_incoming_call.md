---
title: "Trigger - Incoming Call"
source: https://automagic4android.com/trigger_incoming_call_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Incoming Call

The trigger **Incoming Call** is executed when a call is received depending on the criteria defined in the options.

Examples:

- Start recording in Gleeo Time Tracker when your employer calls.
- Send a mail containing the callers number and time to your mail account.

### Settings

#### Incoming call numbers

The list of call numbers when the flow should be executed. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

Warning: The formatting of the incoming number depends on the operator in use. Some operators format the number as an international callnumber like +17001111111, local fixed line network numbers often use the local format.
You have to check the log file to see the exact formatting used or you can add an action **Notification on Screen** with text `{incoming_number}` to see the actual number.

#### Phone state

Defines the state of the call to trigger the flow. Selecting multiple states triggers the flow once for each state.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `incoming_number` — the number of the calling party or null when suppressed
- `call_state` — the state of the call (IDLE, RINGING, OFFHOOK)
- `call_missed_rejected` — true or false whether or not the call has been missed or rejected when the phone enters the idle state
- `contact_name` — the name of the contact if available
- `contact_company` — the company of the contact if available
- `contact_title` — the title of the contact if available
- `contact_note` — the note of the contact if available
- `contact_nickname` — the nickname of the contact if available
- `contact_email` — an email address of the contact if available
- `contact_groups` — the list of groups of the contact if available

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
