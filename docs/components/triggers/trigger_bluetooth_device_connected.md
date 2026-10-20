---
title: "Trigger - Bluetooth Device Connected"
source: https://automagic4android.com/trigger_bluetooth_device_connected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Bluetooth Device Connected

The trigger **Bluetooth Device Connected** is executed when a bluetooth device is connected.

Examples:

- Turn down the volume when a bluetooth headset is connected.

### Settings

#### Bluetooth Device

Defines whether the trigger should be executed for all devices or only for a specific device.

#### Bluetooth Device Address

The address of the bluetooth device.

#### Bluetooth Device Name

The name of the bluetooth device.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `name` — the name of the device
- `address` — the address of the device
- `bluetooth_class` — the bluetooth class of the device
- `bond_state` — the bonding state of the device

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
