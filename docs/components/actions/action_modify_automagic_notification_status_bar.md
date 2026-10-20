---
title: "Action - Modify Automagic Notification on Statusbar"
source: https://automagic4android.com/action_modify_automagic_notification_status_bar_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Modify Automagic Notification on Statusbar

The action **Modify Automagic Notification on Statusbar** modifies the permanent notification usually shown by Automagic for technical reasons. The appearance of a modified notification is reset to the default when one of the settings in Automagic pertaining to the notification is changed.

Examples:

- Show a different icon when a particular flow is running.

### Settings

#### Icon

The icon to use for this notification.

Custom icons are supported starting with Android 6.

Note: Android will usually show all non-transparent parts as white so it's recommended to create custom PNG images with a transparent background and a white color to paint the contents.
Note: Option 'Custom icon' can lead to crashes on some devices with Android 6.0.

#### Title

The title of the notification. [Variables are supported.](action_script.md#string-inline-expressions)

#### Message

The message of the notification. [Variables are supported.](action_script.md#string-inline-expressions)

#### Accent color

The color used by the device for in the notification (usually the background color of the icon in the expanded statusbar).

#### Category (Android 5+)

The category of the notification. The category defines if a notification is allowed to pass the interruptions filter.

#### Priority (Android 4.1+)

Defines the priority of the notification. A notification with a low priority might be displayed in the expanded statusbar only (depends on Android version).

#### Visibility (Android 5+)

Whether notifications are secret, private or public which defines whether the notifications are displayed on the lock screen or not. The Lock screen must also be configured appropriately.

#### Big Message (Android 4.1+)

Defines a big message that will be displayed when the notification is expanded (by swiping down on the notification). The notification usually also shows the big message when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progressbar

Defines whether a progressbar should be shown in the notification.

#### Indeterminate progress

Whether the progress should be indeterminate.

#### Progressbar value / Max value

The current value of the progress and the maximum value (100%). [Variables are supported.](action_script.md#string-inline-expressions)

#### Large Icon (Android 3+)

Defines whether a large icon should be displayed in the notification. [Variables are supported.](action_script.md#string-inline-expressions)

#### Group (Android 7+)

Defines the group of this notification. [Variables are supported.](action_script.md#string-inline-expressions)

#### Group summary (Android 7+)

Defines whether this notification is the group summary for this group. [Variables are supported.](action_script.md#string-inline-expressions)

#### Actions (Android 4.1+)

Up to three actions displayed as buttons when the notification is expanded (by swiping down on the notification). The notification usually also shows the action buttons when the notification is displayed as the topmost notification on the notification drawer. You can affect the ordering of the notifications by using the priority setting.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
