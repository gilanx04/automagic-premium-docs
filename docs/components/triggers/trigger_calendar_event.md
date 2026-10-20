---
title: "Trigger - Calendar Event"
source: https://automagic4android.com/trigger_calendar_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Calendar Event

The trigger **Calendar Event** is executed when an event on the calendar starts or ends.

Examples:

- Mute the ringer when a meeting starts.
- Vibrate 5 minutes before a meeting starts.
- Start recording a task in *Gleeo Time Tracker* when a meeting starts.

### Settings

#### Trigger at Event Start

Whether the trigger should execute at the start of the event. The duration specifies whether the trigger should execute a certain amount of time before or after the event begins.

#### Trigger at Event End

Whether the trigger should execute at the end of the event. The duration specifies whether the trigger should execute a certain amount of time before or after the event ends.

#### Calendars

A comma separated list of calendar names that should be checked for events. The names can contain glob pattern characters like `*` and `?`.

#### Titles

A comma separated list of event titles to match. The titles can contain glob pattern characters like `*` and `?`.

Examples:

- `Plan*` matches titles like `Planning`, `Plan B` etc.

#### Descriptions

A comma separated list of event descriptions to match. The descriptions can contain glob pattern characters like `*` and `?`.

#### Locations

A comma separated list of event locations to match. The locations can contain glob pattern characters like `*` and `?`.

#### Event Type

Whether the trigger should consider all day events or regular events (not all day) or both.

#### Event Availability

Whether the trigger should consider events marked as free, busy or tentative.

#### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../../reference/device-idle-mode.md))

#### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `event_calendar` — the name of the calendar of the event
- `event_title` — the title of the event
- `event_description` — the description of the event
- `event_location` — the location of the event
- `event_start` — the start time of the event
- `event_end` — the end time of the event
- `event_all_day` — boolean indicating if the event is all day or not
- `event_availability` — FREE, BUSY or TENTATIVE depending on the availability of the event
- `event_id` — the ID of the event

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
