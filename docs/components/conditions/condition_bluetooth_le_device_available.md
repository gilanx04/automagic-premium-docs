---
title: "Condition - Bluetooth LE Device Available"
source: https://automagic4android.com/condition_bluetooth_le_device_available_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Bluetooth LE Device Available

The condition **Bluetooth LE Device Available** executes a BT LE scan to test if a device is currently available.

Examples:

- Scan every 10 minutes if a BT LE beacon is available to turn WiFi on at home.

### Settings

#### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Bluetooth Device Name

The name of the bluetooth device.

#### Timeout

The maximum duration of the scan. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `rssi` — measured signal strength, 0 when not available

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
