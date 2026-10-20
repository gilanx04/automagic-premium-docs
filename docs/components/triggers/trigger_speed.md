---
title: "Trigger - Speed"
source: https://automagic4android.com/trigger_speed_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Speed

The trigger **Speed** is executed when the measured speed of the GPS receiver rises above or declines below a certain level.

Warning: This trigger uses the GPS receiver and might increase battery usage (depending on device model).

Examples:

- Record the location in a file whenever you are driving faster than 120km/h.

### Settings

#### Type

- **Declines below**: executes the trigger when the reported speed falls under a certain value
- **Rises above**: executes the trigger when the reported speed rises above a certain value

#### Speed

The speed to compare.

#### Unit

The unit of the speed.

#### Threshold

The minimal change in speed before the trigger is executed again.

Example:
Type: **Declines below**, Speed **40km/h**, Threshold: **10km/h**
The trigger is executed when the speed declines under 40km/h. The speed has to rise to at least 50km/h again before the trigger is executed again.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `location` — the reported location
- `location_accuracy` — the accuracy of the location
- `location_altitude` — the altitude of the location when available
- `location_bearing` — the direction of travel in degrees East of true North when available
- `location_speed` — the speed of travel in meters per second

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
