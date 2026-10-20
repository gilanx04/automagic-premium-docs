---
title: "Trigger - Calendar"
source: https://automagic4android.com/trigger_calendar_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Calendar

The trigger **Calendar** is executed on the defined date and time.

Examples:

- Send a reminder mail on the last Friday of each month.
- Export and mail your time tracking data on the first Monday of each month.

Note: You can use the trigger **Time** to execute a flow on every weekday or on every Monday.

### Settings

#### Date/Time

Defines the date and time when the flow should be executed or the first time a flow should be executed when this is a repeating trigger.

#### Repeats

Defines when this trigger should repeat.

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
