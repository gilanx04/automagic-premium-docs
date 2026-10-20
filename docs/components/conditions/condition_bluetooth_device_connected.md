---
title: "Condition - Bluetooth Device Connected"
source: https://automagic4android.com/condition_bluetooth_device_connected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Bluetooth Device Connected

The condition **Bluetooth Device Connected** checks whether a connection to a Bluetooth device exists.

Warning: This function is not directly supported by Android. The list of currently connected Bluetooth devices is collected using connect/disconnect events reported to Automagic.
Under certain circumstances, the list of connected devices might not correspond to the list of really connected devices, for example when Automagic is freshly installed and a bluetooth device was already connected. In such cases, the bluetooth adapter must be disabled temporarily and reenabled in the preferences of Android to force the Bluetooth devices to reconnect.

Examples:

- Turn on WiFi in the evening only when one of the Bluetooth devices at home is connected.

### Settings

#### Bluetooth Device

Defines whether the condition should check if at least one connection to a device exists or if the condition should check a specific device.

#### Bluetooth Device Address

The address of the bluetooth device. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Bluetooth Device Name

The name of the bluetooth device.

#### Bluetooth Profile

Defines the type of connection to check. Not all device support all types.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `connected_devices_addresses` — list of addresses of the connected devices
- `connected_devices_names` — list of names of the connected devices

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
