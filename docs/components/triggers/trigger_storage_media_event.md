---
title: "Trigger - Storage Media Event"
source: https://automagic4android.com/trigger_storage_media_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Storage Media Event

The trigger **Storage Media Event** is executed when the system mounts or unmounts the SD card or makes other changes involving the storage media.

Examples:

- Disable a flow writing the location to the SD card when the sdcard is removed.

### Settings

#### Event

Defines the event when the flow should be executed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `path` — the affected path

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
