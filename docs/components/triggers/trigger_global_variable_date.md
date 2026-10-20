---
title: "Trigger - Global Variable Date/Time"
source: https://automagic4android.com/trigger_global_variable_date_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Global Variable Date/Time

The trigger **Global Variable Date/Time** is executed when the point of time stored in the global variable is reached.

Examples:

- Execute a flow daily on sunrise/sunset.
- Execute a flow in irregular intervals.

### Settings

#### Global Variable

The name of the global variable containing the point of time.

#### Trigger immediately on missed events

Execute the trigger when the point in time stored in the variable has passed and the trigger did not yet execute the trigger for this point in time (for example when the device was turned off at the date/time specified in the variable or when a past date is assigned to the global variable)

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
