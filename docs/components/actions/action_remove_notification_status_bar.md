---
title: "Action - Remove Notification on Statusbar"
source: https://automagic4android.com/action_remove_notification_status_bar_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Remove Notification on Statusbar

The action **Remove Notification on Statusbar** removes the specified or all notifications on the statusbar added by the action **Notification on Statusbar**.

Example:

- Show a notification when a sound profile is active and remove the notification when the sound profile is deactivated.

### Settings

#### Notification Type

Whether the action should affect only notifications of Automagic or notifications of all apps in general (Android 4.3+)

#### Automagic Notification ID

The ID of the notification to remove. The ID must match the ID used in the action **Notification on Statusbar**. [Variables are supported.](action_script.md#string-inline-expressions)
**All** removes all removable notifications of Automagic irrespective of the ID.

#### Notifications

Whether to remove all removable notifications or only the notifications of the specified app.

#### Package Names

The names of the packages/apps to remove the notifications from. [Variables are supported.](action_script.md#string-inline-expressions)

#### Notification ID

The ID of the notification to remove. [Variables are supported.](action_script.md#string-inline-expressions)
Trigger **Notification on Statusbar Displayed** provides the ID of the notification in variable `id`. Use `{id}` to remove the notification that triggered the flow.

#### Filter

Defines the text that must be contained in one of the available fields. [Variables are supported](action_script.md#string-inline-expressions) for *contains text* and *matches glob*.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
