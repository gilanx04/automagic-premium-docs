---
title: "Trigger - Device Storage Space Low"
source: https://automagic4android.com/trigger_device_storage_space_low_okay_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Device Storage Space Low

The trigger **Device Storage Space Low** executes the flow when the internal device storage space becomes low or the free storage space is back to a normal level.

Note: The amount of free space to consider as low is defined by the device manufacturer.
Standard Android considers less than 10% of free internal memory as low.

Example:

- Play a warning sound when the device storage space is low.

### Settings

#### Device Storage Space

**becomes low**
Executes the flow when the storage space becomes low.

**becomes OK**
Executes the flow when the storage space is back to a normal level.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
