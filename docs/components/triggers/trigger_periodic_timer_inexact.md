---
title: "Trigger - Periodic Timer Inexact"
source: https://automagic4android.com/trigger_periodic_timer_inexact_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Periodic Timer Inexact

The trigger **Periodic Timer Inexact** is executed approximately in the specified interval. The device can adjust the time of the trigger a bit and call the trigger when the device is currently also executing other tasks. This trigger uses less battery than the regular trigger **Periodic Timer**

Examples:

- Check approximately once an hour if a server is online.

### Settings

#### Interval (Inexact)

Defines the time interval between flow executions. Android only supports the times available in this list.

#### Wake device when in sleep mode

Defines whether the device should be woken up from sleep mode.
Disabling this option saves a bit of battery but delays the trigger invocation for an unknown amount of time when the devices is asleep.

#### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

#### Weekdays

The day on which the trigger should be active.

#### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
