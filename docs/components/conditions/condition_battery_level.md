---
title: "Condition - Battery Level"
source: https://automagic4android.com/condition_battery_level_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Battery Level

The condition **Battery Level** checks whether the battery level is above or below a certain level.

Examples:

- Download a file only when the battery level is above 50%.

### Settings

#### Battery Level

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported percentage by the system is below the defined level

**higher than**
true when the reported percentage by the system is above the defined level

**exactly**
true when the reported percentage by the system is exactly on the defined level

**full**
true when the reported battery status by the system is full

#### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

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
- `battery_charge_counter` — Battery capacity in microampere-hours. null when not available
- `battery_current_now` — Instantaneous battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_current_average` — Average battery current in microamperes (positive values=charging, negative values=discharging). null when not available
- `battery_energy_counter` — Battery remaining energy in nanowatt-hours. null when not available

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
