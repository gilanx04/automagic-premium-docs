---
title: "Trigger - Activity Started"
source: https://automagic4android.com/trigger_activity_started_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Activity Started

The trigger **Activity Started** is executed when an activity is moved to the foreground.

Examples:

- Increase the display brightness when Google Maps is started.

### Settings

#### Method

How the activity should be determined. Method **Usage statistics** can be delayed on some devices.

#### Package Name

The package name of the app or comma separated list. Glob patterns are supported.

#### Class Name

The class name of the activity or comma separated list. Glob patterns are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app
- `activity_class` — the class of the activity
- `activity_name` — the display name of the activity

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
