---
title: "Trigger - Proximity Sensor"
source: https://automagic4android.com/trigger_proximity_sensor_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Proximity Sensor

The trigger **Proximity Sensor** is executed when the measured distance of the proximity sensor passes the defined distance.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

### Settings

#### Distance (in cm)

Whether to execute the trigger when the distance passes above or below the defined distance and the distance in cm.

#### Keep device awake

Ensure that the device does not go into deep sleep while the action is executed. This option increases battery consumption and should only be enabled when the proximity sensor stops working when the display is turned off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `proximity` — the measured value of the proximity sensor

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
