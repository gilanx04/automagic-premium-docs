---
title: "Trigger - GPS Status Event"
source: https://automagic4android.com/trigger_gps_status_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - GPS Status Event

The trigger **GPS Status Event** is executed, when the system start or stops to use GPS.

Examples:

- Vibrate when the system begins to use GPS for information purposes.

### Settings

#### GPS Status Event

The type of the event:

- **Started**: executes the trigger when the system starts to use GPS
- **Stopped**: executes the trigger when the system stops to use GPS
- **First fix received**: executes the trigger when the system uses GPS and the first fix has just been determined
- **Satellite status changed**: executes the trigger when the satellite status changes (usually very frequent)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `gps_event_type` — typ of the event (1=started, 2=stopped, 3=first fix, 4=satellite status)
- `satellites` — list containing strings each containing the information of one satellite
- `time_to_first_fix` — number of milliseconds between turning on GPS and receiving the first fix, contains 0 or the last value when no fix was determined yet

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
