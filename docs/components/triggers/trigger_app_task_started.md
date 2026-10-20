---
title: "Trigger - App Task Started"
source: https://automagic4android.com/trigger_app_task_started_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - App Task Started

The trigger **App Task Started** is executed when an application is moved to the foreground or opened respectively the user moved the focus to this app.

Examples:

- Lower the media volume when you open the browser.
- Raise the display brightness when you start using Google Maps.

### Settings

#### Method

How the app should be determined. Method **Usage statistics** can be delayed on some devices.

#### Package Name

Enter the name of the package of the application or use the button to show a list of available applications. Glob patterns (\*, ?) can be used to match apps with similar names. A single \*-character matches all apps.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `package_name` — the name of the package
- `app_name` — the display name of the app

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
