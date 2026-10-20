---
title: "Condition - Device Orientation"
source: https://automagic4android.com/condition_device_orientation_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Device Orientation

The condition **Device Orientation** checks whether the device is in one of the specified orientation.

Examples:

- Beep every 5 minutes when recording your time but only when the device display is not facing down.

### Settings

#### Device Orientation

The desired orientation of the device.

- **Face down:** The display of the device is facing down for example when lying on a table with the display towards the table.
- **Face up:** The display of the device is facing up for example when lying on a table with the display facing away from the table.
- **Face left:** The display faces to the left with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Face right:** The display faces to the right with the longer side lying on a table when the upper edge of the device is pointing away from you.
- **Standing upright:** The device is standing upright on a table.
- **Standing upside-down:** The device is standing upside-down on a table.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `accel_x` — the measured acceleration in m/s^2 on the X-axis
- `accel_y` — the measured acceleration in m/s^2 on the Y-axis
- `accel_z` — the measured acceleration in m/s^2 on the Z-axis

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
