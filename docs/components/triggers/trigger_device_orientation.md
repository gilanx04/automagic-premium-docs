---
title: "Trigger - Device Orientation"
source: https://automagic4android.com/trigger_device_orientation_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Device Orientation

The trigger **Device Orientation** executes the flow when the device is moved to the defined orientation.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Reduce the ringer volume when the device screen is facing down.

### Settings

#### Device Orientation

The desired orientation of the device.

- **Face down:** The display of the device is facing down for example when lying on a table with the display towards the table.
- **Face up:** The display of the device is facing up for example when lying on a table with the display facing away from the table.
- **Face left:** The display faces to the left with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Face right:** The display faces to the right with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Standing upright:** The device is standing upright on a table.
- **Standing upside-down:** The device is standing upside-down on a table.

#### Negate

Whether the condition should be negated or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
