---
title: "Trigger - Power Source (Android Wear)"
source: https://automagic4android.com/trigger_power_connected_wear_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Power Source (Android Wear)

The trigger **Power Source (Android Wear)** is executed when a power source is connected to the device (charger or USB cable).

Examples:

- Turn on WiFi when a power source is connected.
- Increase the screen brightness when a power source is connected.
- Set screen brightness to automatic when a power source is disconnected.

### Settings

#### Android Wear device

The target device.

#### Power connected/disconnected

**Connected**
When selected executes the flow when a power source is connected.

- **AC Adapter**: when charging with the AC adapter
- **USB**: when charging over an USB connection
- **Wireless**: when charging wirelessly

**Disconnected**
When selected executes the flow when a power source is disconnected.

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
- `battery_health` — the health of the battery
- `node_id` — the ID of the Wear node

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
