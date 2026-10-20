---
title: "Trigger - Dock Event"
source: https://automagic4android.com/trigger_dock_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Dock Event

The trigger **Dock Event** is executed when the device is put into a dock (car, desk, some external hardware keyboard).

The dock type can be distinguished using a condition **Dock State**.

Examples:

- Raise the audio volume when the device is put into a dock.

### Settings

#### Docked/Undocked

**Docked**
When selected executes the flow after the device has been put into a dock.

**Undocked**
When selected executes the flow after the device has been removed from a dock.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `dock_state` — the state/dock type

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
