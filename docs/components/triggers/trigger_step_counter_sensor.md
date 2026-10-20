---
title: "Trigger - Step counter"
source: https://automagic4android.com/trigger_step_counter_sensor_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Step counter

The trigger **Step counter** uses the Step counter/Pedometer of the device and executes a flow when the specified number of steps have been counted. The device can optimise the battery usage and inform Automagic less often when the display is turned off.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices do not count the steps when the screen is off.

Examples:

- Create a calendar event 'Training highly recommended' for the next day when less than 1000 steps have been counted for the day.

### Settings

#### On every nth step (or less frequent)

Defines after how many steps a flow should be executed. The step counter can inform Automagic less often to save battery.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `step_count` — the number of steps since the trigger was enabled
- `step_count_total` — the number of steps counted by the sensor since the last reboot
- `last_step_time` — the point in time of the last detected step. Automagic attempts to provide a regular system time but might fail on some devices due to differences on ROMs.

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
