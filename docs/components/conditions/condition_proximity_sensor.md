---
title: "Condition - Proximity Sensor"
source: https://automagic4android.com/condition_proximity_sensor_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Proximity Sensor

The condition **Proximity Sensor** checks whether the measured distance of the proximity sensor is below or above the defined distance.

Warning: Some devices turn off the sensors when the screen is off.
Warning: Some devices can not determine the current value of the sensor and only deliver a value when the measured value of the sensor changes. This condition does not work on such devices.

### Settings

#### Distance (in cm)

Whether the condition should check if the distance is above or below the defined distance and the distance in cm.

#### Timeout

The amount of time to wait for a value of the sensor, the condition is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `proximity` — the measured value of the proximity sensor

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
