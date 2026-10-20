---
title: "Trigger - Pressure Sensor"
source: https://automagic4android.com/trigger_pressure_sensor_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Pressure Sensor

The trigger **Pressure Sensor** is executed when the measured pressure of the pressure sensor rises above or declines below a certain level or when the pressure changes at least the specified amount in the given time.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Tip: If you need to check the pressure only every few minutes, it is recommended to use a condition **Pressure Sensor** since the condition will not use the sensor constantly and thus consumes less battery.

Examples:

- Execute a flow when the pressure changes when walking down a stair.

### Settings

#### Type

- **Declines below**: executes the trigger when the measured pressure falls under a certain value
- **Rises above**: executes the trigger when the measured pressure rises above a certain value
- **Declines within duration**: executes the trigger when the measured pressure declines a certain amount within a given time
- **Rises within duration**: executes the trigger when the measured pressure rises a certain amount within a given time

#### Pressure (in mbar)

The pressure in millibar to compare.

#### Threshold

The minimal change in pressure before the trigger is executed again.

Example:
Type: **Declines below**, Pressure **1000mbar**, Threshold: **5mbar**
The trigger is executed when the pressure declines below 1000mbar. The pressure has to rise to at least 1005mbar again before the trigger is executed again.

#### Change (in mbar)

The change in pressure in mbar.

#### Duration

The duration the pressure change has to happen for the trigger to execute.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `pressure` — the measured pressure in mbar

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
