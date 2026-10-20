---
title: "Trigger - Hardware Key Event"
source: https://automagic4android.com/trigger_key_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Hardware Key Event

The trigger **Hardware Key Event** is executed when the specified key is pressed/released. Most devices usually only provide hardware keys for volume up and volume down. The power key can usually not be intercepted.

Examples:

- Scroll down in a browser window when the volume down key is pressed.

### Settings

#### Keys

The list of names of keys that should execute the trigger. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Actions

Whether down, up or both actions should execute the trigger.

#### Block event (blocks down and up actions)

Whether or not the key event should be blocked so that the system does not send the key event to other apps.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `key_code` — the numeric keycode
- `key_code_name` — the name of the keycode
- `key_duration` — the duration of the event in milliseconds
- `key_source_device_id` — the ID of the sending device
- `key_action_down` — whether the action was down
- `key_action_down` — whether the action was up

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
