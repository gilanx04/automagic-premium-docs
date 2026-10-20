---
title: "Action - Init Variable Next Alarm"
source: https://automagic4android.com/action_init_variable_next_alarm_en.html
archived: 2022-10-06
archive_url: https://web.archive.org/web/20221006132519/https://automagic4android.com/action_init_variable_next_alarm_en.html
category: action
---

# Action - Init Variable Next Alarm

The action **Init Variable Next Alarm** fills the time of the next currently known alarm into the specified variable.

Warning: This function is not officially supported by Android < 5.0 and might not work on all devices.

Examples:

- Get the time of the next alarm to show a reminder one hour before the alarm is reached.

### Settings

#### Variable

The name of the variable.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `next_alarm` — the time of the next alarm or null when no alarm is set

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
