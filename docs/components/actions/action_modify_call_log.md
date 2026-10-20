---
title: "Action - Modify Call Log"
source: https://automagic4android.com/action_modify_call_log_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Modify Call Log

The action **Modify Call Log** marks the entries of the call log as acknowledged or clears the call log.

Examples:

- Delete the call log every Monday morning.

### Settings

#### Operation

if the entries should be marked as acknowledged or if the call log should be cleared.

#### Numbers

The list of call numbers to delete. Multiple numbers can be separated by commas.
Glob patterns (\*, ?) can be used to filter on similar numbers like corporate number ranges:

Examples:

- +17001111111
- +17001111111,+17002222222
- \*70033311\*
- \*70033311\*,\*70033?22\*

Special characters like `+`, `-` and `.` are removed before comparing the number.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
