---
title: "Trigger - Light Sensor"
source: https://automagic4android.com/trigger_light_sensor_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Light Sensor

The trigger **Light Sensor** is executed when the measured surrounding light intensity passes the defined value.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

### Settings

#### Sensitivity

The sensitivity of the slider to define the light level.

#### Light Level

Whether the trigger should execute when the illuminance passes above or below a certain value and the level to use.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `light_level` — the effective illuminance in lux

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
