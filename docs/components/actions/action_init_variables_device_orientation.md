---
title: "Action - Init Variables Device Orientation"
source: https://automagic4android.com/action_init_variables_device_orientation_en.html
archived: 2022-10-07
archive_url: https://web.archive.org/web/20221007121922/https://automagic4android.com/action_init_variables_device_orientation_en.html
category: action
---

# Action - Init Variables Device Orientation

The action **Init Variables Device Orientation** measures the device orientation using the accelerometer and magnetometer sensors of the device.

Warning: This action uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Show your current orientation value in a popup.
- Select the task to record by changing the device orientation.

### Settings

#### Variable for Azimuth

The name of the variable to store the azimuth of the device (in degrees).

#### Variable for Pitch

The name of the variable to store the pitch of the device (in degrees).

#### Variable for Roll

The name of the variable to store the roll of the device (in degrees).

#### Timeout

The amount of time to wait for a value of the sensor, the action is terminated with an error when no value becomes available.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `azimuth` — the azimuth in degrees
- `pitch` — the pitch in degrees
- `roll` — the roll in degrees

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
