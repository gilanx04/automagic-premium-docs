---
title: "Trigger - Audio Volume"
source: https://automagic4android.com/trigger_audio_volume_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Audio Volume

The trigger **Audio Volume** is executed when the volume of the device has been changed. Some devices report the volume change slightly delayed.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Vibrate whenever the volume is changed.

### Settings

#### Sound Type

The type of the audio stream to check.

#### Condition

Whether the condition should check if the volume is above or below the volume level.

#### Volume

The volume value to check.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `volume` — the new volume value
- `old_volume` — the volume value before the change

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
