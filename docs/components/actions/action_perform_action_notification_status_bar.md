---
title: "Action - Perform Action on Notification on Statusbar"
source: https://automagic4android.com/action_perform_action_notification_status_bar_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Perform Action on Notification on Statusbar

The action **Perform Action on Notification on Statusbar** clicks the notification or one of the action buttons which are usually available in the big, expanded notification on Android 4.1+.
The flow must be executed by a trigger **Notification on Statusbar Displayed** or the action after a condition **Notification on Statusbar Displayed** otherwise Automagic has no possibility to access the notification.

Warning: Android 4.1+ is required. This function is not officially supported by Android and might not work on all devices.

Examples:

- Automatically archive a mail when the mail contains a specific text.

### Settings

#### Action Type

Whether to perform a click on the notification or to perform a click on a button of the notification or to execute an action of a wearable.

#### Button

The label of the button to click. The label needs to match the entered text exactly. [Variables are supported.](action_script.md#string-inline-expressions)

#### Wearable Action

The name of the wearable action. [Variables are supported.](action_script.md#string-inline-expressions)

#### Input

The text to pass to the wearable action (only takes effect when the action allows text input). [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
