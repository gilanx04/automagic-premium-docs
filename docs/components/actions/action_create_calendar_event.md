---
title: "Action - Create Calendar Event"
source: https://automagic4android.com/action_create_calendar_event_en.html
archived: 2024-04-19
archive_url: https://web.archive.org/web/20240419034046/https://automagic4android.com/action_create_calendar_event_en.html
category: action
---

# Action - Create Calendar Event

The action **Create Calendar Event** creates an event on the specified calendar of the device (Android 4+ required)

Examples:

- Create a calendar event based on the text of a received SMS.
- Create a calendar event for every received call.

### Settings

#### Calendar

The name of calendar to create the event in. [Variables are supported.](action_script.md#string-inline-expressions)

#### Start/End Type

Whether the event should be created relative to the time when the action is executed or absolute.

#### Start in

The start offset of the event from now. *1h* creates an event that starts in one hour. [Variables are supported.](action_script.md#string-inline-expressions)

#### Duration

The desired duration of the event like *1h* or *45m*. [Variables are supported.](action_script.md#string-inline-expressions)

#### From

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the start time of the event.

#### To

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the end time of the event.

#### All day

When checked creates an event lasting the whole day, the event spans all days intersecting the time span specified in *Start in/Duration* or *From/To*.

#### Title

The title. [Variables are supported.](action_script.md#string-inline-expressions)

#### Description

The description. [Variables are supported.](action_script.md#string-inline-expressions)

#### Location

The event location. [Variables are supported.](action_script.md#string-inline-expressions)

#### Reminders

The reminders to create. [Variables are supported.](action_script.md#string-inline-expressions)

#### Event Availability

The availability (not all calendars support Tentative).

#### Visibility

The visibility.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
