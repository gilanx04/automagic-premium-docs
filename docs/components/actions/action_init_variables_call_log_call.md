---
title: "Action - Init Variables Call Log"
source: https://automagic4android.com/action_init_variables_call_log_call_en.html
archived: 2024-04-20
archive_url: https://web.archive.org/web/20240420135216/https://automagic4android.com/action_init_variables_call_log_call_en.html
category: action
---

# Action - Init Variables Call Log

The action **Init Variables Call Log** initializes variables with the values of the last entry of the call log.

Examples:

- Update a widget with the values of the last call.

### Settings

#### Query Criteria

Specifies which call should be stored in the variables.

#### Variable for Call Number

The name of the variable to store the call number.

#### Variable for Call Date/Time

The name of the variable to store the point in time of the call.

#### Variable for Call Duration

The name of the variable to store the call duration.

#### Variable for Call Type

The name of the variable to store the call type (1=incoming, 2=outgoing, 3=missed).

#### Variable for Call Contact Name

The name of the variable to store the contact name.

#### Variable for Call New Flag

The name of the variable to store if the call log entry has not been marked acknowledged.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `call_number` — the call number
- `call_time` — the time of the call in millis since 1970
- `call_duration` — the call duration in seconds
- `call_type` — the call type (1=incoming, 2=outgoing, 3=missed)
- `call_cached_name` — the name of the contact (might be outdated when the contact has been modified in the contacts afterwards)
- `call_new` — true or false whether the entry in the call log has not been acknowledged yet

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
