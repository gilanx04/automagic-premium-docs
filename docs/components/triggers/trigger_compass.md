---
title: "Trigger - Compass"
source: https://automagic4android.com/trigger_compass_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Compass

The trigger **Compass** executes the flow when the device changes its orientation.

Warning: This trigger uses the device hardware sensors and might increase battery usage (depending on device model). Some devices turn off the sensors when the screen is off.

Examples:

- Play a beep sound when the device is heading north.

### Settings

#### Type

The type of the trigger.

- **Periodic**: executes the flow in periodic time intervals
- **On Change**: executes the flow when the orientation changed for at least some degrees.
- **On Relative Sector Change**: Remembers the device orientation when this trigger is enabled first, divides the orientation into the specified number of equal sectors and executes the flow whenever the device stays in a different sector.

#### Frequency

Defines the frequency between flow executions.

#### Tolerance in Degrees

The minimum amount of change in the device orientation required to execute the flow.

#### trigger when steady

Executes the flow only when the device does not change the direction for a short period of time anymore.

#### Number of Sectors

The number of equal sectors to divide the orientation of the device. The sectors are numbered starting at 1 and incrementing in clockwise order.

Example:
When 4 sectors are desired the 360° possible degrees are divided into 4 sectors with an opening angle of 90° each. The sectors are relative to the initial device orientation when the trigger was enabled.

- Sector 1: 315° to 45°
- Sector 2: 45° to 135°
- Sector 3: 135° to 225°
- Sector 4: 225° to 315°

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `azimuth` — the azimuth in degrees
- `pitch` — the pitch in degrees
- `roll` — the roll in degrees
- `azimuth_sector` — the azimuth sector (1 to Number of Sectors)
- `pitch_sector` — the pitch sector (1 to Number of Sectors)
- `roll_sector` — the roll sector (1 to Number of Sectors)

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
