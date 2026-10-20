---
title: "Trigger - Time"
source: https://automagic4android.com/trigger_time_en.html
archived: 2022-12-02
archive_url: https://web.archive.org/web/20221202220613/https://automagic4android.com/trigger_time_en.html
category: trigger
---

# Trigger - Time

The trigger **Time** executes the flow regularly on the specified weekday and time.

Examples:

- Download a PDF newspaper every morning at 6am.
- Turn on airplane mode every evening at 11pm.
- Turn off airplane mode every morning at 6am.

### Settings

#### Weekdays

The day on which the trigger should execute the flow.

#### Time

The time of the day when the trigger should execute the flow.

#### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../../reference/device-idle-mode.md))

#### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
