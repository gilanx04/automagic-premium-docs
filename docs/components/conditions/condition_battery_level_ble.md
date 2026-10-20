---
title: "Condition - Battery Level BLE (Experimental)"
source: https://automagic4android.com/condition_battery_level_ble_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Battery Level BLE (Experimental)

The condition **Battery Level BLE (Experimental)** checks the battery level of a Bluetooth LE device that supports the standardized Battery service.

Warning: Bluetooth LE is not working reliable on many Android ROMs. Restarting the device or turning Bluetooth off and on again can help when the condition does not work.

Examples:

- Check once a week if the battery of the Polar heart rate sensor is still OK.

### Settings

#### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Bluetooth Device Name

The name of the bluetooth device.

#### Battery Level

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported percentage by the device is below the defined level

**higher than**
true when the reported percentage by the device is above the defined level

**exactly**
true when the reported percentage by the device is exactly on the defined level

#### Level Percentage

Defines the level percentage.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `battery_level` — the charging level of the battery
- `battery_percentage` — the charging percentage

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
