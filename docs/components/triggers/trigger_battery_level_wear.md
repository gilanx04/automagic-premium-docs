---
title: "Trigger - Battery Level (Android Wear)"
source: https://automagic4android.com/trigger_battery_level_wear_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Battery Level (Android Wear)

The trigger **Battery Level (Android Wear)** is executed whenever the battery level changes and the built in condition about the level holds true.

Examples:

- Lower the display brightness when the battery level falls below 50%.
- Turn off WiFi when the battery level falls below 30%.

### Settings

#### Android Wear device

The target device.

#### Battery Level

Defines the condition that must be met to execute the flow:

**becomes lower than**
Executes the flow when the last reported percentage was above the defined level and the current percentage is below the defined level

**becomes higher than**
Executes the flow when the last reported percentage was below the defined level and the current percentage is above the defined level

**becomes equal to**
Executes the flow when the last reported percentage was different than the defined level and the current percentage equals the defined level

**becomes full**
Executes the flow when the last reported battery status was not full and is now full

**lower than**
Executes the flow whenever the reported percentage by the system is below the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**higher than**
Executes the flow whenever the reported percentage by the system is above the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**exactly**
Executes the flow whenever the reported percentage by the system is exactly on the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last percentage has been the same.

**full**
Executes the flow whenever the reported battery status by the system is full. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last status has been already full.

#### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage
- `battery_plugged` — whether the battery is plugged (1=AC adapter, 2=USB, 4=Wireless) or not (0=not plugged)
- `battery_present` — whether the battery is present or not
- `battery_scale` — the maximum battery level
- `battery_status` — the status of the battery (1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full)
- `battery_technology` — the technology of the battery
- `battery_temperature` — the temperature of the battery (in tenths of degree Celsius)
- `battery_voltage` — the current battery voltage
- `battery_health` — the health of the battery (1=unknown, 2=good, 3=overheat, 4=dead, 5=over voltage, 6=unspecified failure, 7=cold)
- `node_id` — the ID of the Wear node

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
