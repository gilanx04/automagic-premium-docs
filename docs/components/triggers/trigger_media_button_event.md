---
title: "Trigger - Media Button Event (Experimental)"
source: https://automagic4android.com/trigger_media_button_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Media Button Event (Experimental)

The trigger **Media Button Event (Experimental)** executes a flow when the system detects a media button event, for example when the play-button is pressed on a headset.

Warning: When an audio player is launched, future events are usually sent to the audio player and not to Automagic anymore. If this is not the desired behaviour, Automagic has to be registered to receive the events again using an action **Reregister Media Button Receiver**.

### Settings

#### Events

Whether the trigger should be executed for all media button events or only for a specific button.

#### Specific event

The Event/Button that should be reacted upon.
Wired headsets usually generate the event *Headset Hook*.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `key_code` — the numeric keycode
- `key_code_name` — the name of the keycode
- `key_duration` — the duration of the event in milliseconds
- `key_source_device_id` — the ID of the sending device

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
