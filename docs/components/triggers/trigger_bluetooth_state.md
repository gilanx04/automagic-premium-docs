---
title: "Trigger - Bluetooth State"
source: https://automagic4android.com/trigger_bluetooth_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Bluetooth State

The trigger **Bluetooth State** is executed when the bluetooth adapter of the device is turned on or off depending on the settings used.

Examples:

- Enable some flows using the bluetooth adapter as soon as the bluetooth is turned on.

### Settings

#### Bluetooth state

Defines the bluetooth states to trigger the flow. Selecting multiple states triggers the flow once for each state.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_bluetooth_state` — the state of the bluetooth adapter before
- `bluetooth_state` — the current state of the bluetooth adapter

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
