---
title: "Trigger - Global Variable"
source: https://automagic4android.com/trigger_global_variable_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Global Variable

The trigger **Global Variable** is executed when a different value is assigned to a global variable. The trigger is not executed when the same value is assigned to the variable again.

Examples:

- Show a reminder when you sent more than 10 SMS in one day.

### Settings

#### Global Variable

The name of the global variable to watch.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `old_` — contains the old value of the global variable before it has been updated

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
