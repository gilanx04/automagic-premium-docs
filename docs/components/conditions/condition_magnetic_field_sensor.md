---
title: "Condition - Magnetic Field Sensor"
source: https://automagic4android.com/condition_magnetic_field_sensor_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Magnetic Field Sensor

The condition **Magnetic Field Sensor** checks whether the measured value of the magnetic field sensor is below or above the defined level.

Warning: Some devices turn off the sensors when the screen is off.
Warning: Some devices can not determine the current value of the sensor and only deliver a value when the measured value of the sensor changes. This condition does not work on such devices.

Examples:

- Execute some actions only when the device is placed near a magnet.

### Settings

#### Sensitivity

The sensitivity of the slider to define the field strength.

#### Magnetic Field Strength

Whether the trigger should execute when the illuminance passes above or below a certain value and the level to use.

#### Timeout

The amount of time to wait for a value of the sensor, the condition is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `magnetic_field_strength` — the measured strength in micro Tesla

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
