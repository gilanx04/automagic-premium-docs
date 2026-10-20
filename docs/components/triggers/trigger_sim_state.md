---
title: "Trigger - SIM State"
source: https://automagic4android.com/trigger_sim_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - SIM State

The trigger **SIM State** is executed when the SIM state changes to one of the selected states.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play a warning sound when the SIM is removed.

### Settings

#### SIM state changed to

Defines the SIM states to execute the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_sim_state` — the previous state (0=unknown, 1=absent, 2=PIN required, 3=PUK required, 4=network locked, 5=ready)
- `sim_state` — the new state (0=unknown, 1=absent, 2=PIN required, 3=PUK required, 4=network locked, 5=ready)

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
