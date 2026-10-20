---
title: "Trigger - Notification on Statusbar Selected"
source: https://automagic4android.com/trigger_notification_status_bar_selected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Notification on Statusbar Selected

The trigger **Notification on Statusbar Selected** executes the flow when a notification is selected that was previously shown using action **Notification on Statusbar**.

Example:

- Show a notification when the airplane mode is enabled by a flow. Turn airplane mode manually off when the notification in the statusbar is selected.

### Settings

#### Notification

**Create own Notification**
Creates a new notification on the statusbar.

**Trigger on Notification from Action**
Trigger the flow when a notification supplied by action **Notification on Statusbar** was selected.

#### Icon

The icon to use for this notification.

Custom icons are supported starting with Android 6.

Note: Android will usually show all non-transparent parts as white so it's recommended to create custom PNG images with a transparent background and a white color to paint the contents.
Note: Option 'Custom icon' can lead to crashes on some devices with Android 6.0.

#### Title

The title of the notification.

#### Message

The message of the notification.

#### Play Sound

Plays the default notification sound when checked.

#### Vibrate

Vibrates when checked.

#### Flash LED

Flash the notification LED using the supplied color and blink rate. Notification LED and user defined colors are not supported on all devices.

#### Accent color

The color used by the device for in the notification (usually the background color of the icon in the expanded statusbar).

#### Ongoing

Flags this notification as an ongoing event and prevents the removal of this notification from the statusbar. A notification ID is mandatory when this option is selected.

#### Category (Android 5+)

The category of the notification. The category defines if a notification is allowed to pass the interruptions filter.

#### Priority (Android 4.1+)

Defines the priority of the notification. A notification with a low priority might be displayed in the expanded statusbar only (depends on Android version).

#### Visibility (Android 5+)

Whether notifications are secret, private or public which defines whether the notifications are displayed on the lock screen or not. The Lock screen must also be configured appropriately.

#### Notification IDs

Whether the trigger should be executed for one specific ID or for all notifications. The ID can be defined in the action **Notification on Statusbar**.

#### Big Message (Android 4.1+)

Defines a big message that will be displayed when the notification is expanded (by swiping down on the notification). The notification usually also shows the big message when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

#### Large Icon (Android 3+)

Defines whether a large icon should be displayed in the notification.

#### Group (Android 7+)

Defines the group of this notification.

#### Group summary (Android 7+)

Defines whether this notification is the group summary for this group.

#### Actions (Android 4.1+)

Up to three actions displayed as buttons when the notification is expanded (by swiping down on the notification). The notification usually also shows the action buttons when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `notification_title` — the title of the notification
- `notification_message` — the message of the notification
- `notification_id` — the ID of the selected notification

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
