---
title: "Condition - Calendar Event"
source: https://automagic4android.com/condition_calendar_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Calendar Event

The condition **Calendar Event** checks, whether an event on the calendar is currently active.

Examples:

- Send an SMS to the calling number telling when your meeting ends.
- Don't let the SMS be read aloud in a meeting.

### Settings

#### Starting

The start time offset the condition should consider an event as active.

#### Ending

The end time offset the condition should consider an event as active.

#### Calendars

A comma separated list of calendar names that should be checked for events. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Titles

A comma separated list of event titles to match. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

Examples:

- `Plan*` matches titles like `Planning`, `Plan B` etc.

#### Descriptions

A comma separated list of event descriptions to match. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Locations

A comma separated list of event locations to match. The values can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Event Type

Whether the trigger should consider all day events or regular events (not all day) or both.

#### Event Availability

Whether the trigger should consider events marked as free, busy or tentative.

#### Multiple Events

The event that should be preferred to fill the variables when multiple events match the defined criteria of the condition.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

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

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
