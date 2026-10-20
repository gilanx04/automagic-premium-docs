---
title: "Trigger - Notification on Screen Displayed"
source: https://automagic4android.com/trigger_notification_screen_displayed_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Notification on Screen Displayed

The trigger **Notification on Screen Displayed** is executed when a notification is displayed on the screen.

Note: At least Android 4.0 (ICS) is required.

Examples:

- Read out the text of a notification.

### Settings

#### Package Name

The comma separated list of apps that displayed the notification. Glob patterns can be used to match multiple packages.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `notification_message` — the text of the displayed notification
- `package_name` — the name of the package that displayed the notification
- `app_name` — the display name of the app

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
