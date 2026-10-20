---
title: "Trigger - Periodic Timer"
source: https://automagic4android.com/trigger_periodic_timer_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Periodic Timer

The trigger **Periodic Timer** is executed in the specified interval.

Examples:

- Remind about a recording task in Gleeo Time Tracker every 5 minutes.

### Settings

#### Interval

Defines the time interval between flow executions.

#### Wake device when in sleep mode

Defines whether the device should be woken up from sleep mode.
Disabling this option saves a bit of battery but delays the trigger invocation for an unknown amount of time when the devices is asleep.

#### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

#### Weekdays

The day on which the trigger should be active.

#### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

#### At fixed times

Defines if the timer should execute the flow periodically in the set interval relative to midnight (or at the From-time when a limited time range is in effect).
If this option is not set, the interval starts at the moment when the trigger is enabled.

Examples when a flow is activated at 07:13:

- Option **not set**, Interval 1h: Flow executes at 08:13, 09:13, 10:13, ...
- Option **set**, Interval 1h: Flow executes at 08:00, 09:00, 10:00, ...
- Option **set**, Interval 1h, Time range 07:00 - 09:00: Flow executes at 08:00, 09:00 (next day: 07:00, 08:00, 09:00)
- Option **set**, Interval 1h, Time range 07:30 - 09:30: Flow executes at 07:30, 08:30, 09:30

Note that disabling *Wake device when in sleep mode* can delay the execution when the device is in deep sleep.

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
