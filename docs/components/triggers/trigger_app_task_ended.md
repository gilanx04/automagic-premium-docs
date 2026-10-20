---
title: "Trigger - App Task Ended"
source: https://automagic4android.com/trigger_app_task_ended_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - App Task Ended

The trigger **App Task Ended** is executed when an application is moved to the background or closed respectively the user moved the focus to another app.
The application might still be running in the background or the process hosting the application might still be in memory.

Examples:

- Raise the media volume back to normal when you leave the browser.
- Change the display brightness back to normal when you don't use Google Maps anymore.

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
