---
title: "Action - Notification on Statusbar"
source: https://automagic4android.com/action_notification_status_bar_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Notification on Statusbar

The action **Notification on Statusbar** shows a notification on the status bar. The notification is displayed until the notification is clicked or clear is pressed.

Examples:

- Show a notification when a background flow sends your location by mail.

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

#### Channel (Android 8+)

The ID of the notification channel to use. [Variables are supported.](action_script.md#string-inline-expressions)
Apps can not change the channel settings once the channel has been created. Use the button **Channel settings…** to change the settings once the channel has been created or use an action **Modify Notification Channel** to change the settings on supported devices.
The initial channel settings are inferred from the settings in the notification action based on the settings like **Play Sound**, **Vibrate**, **Flash LED**, **Priority** and **Visibility**.

#### Play Sound

Plays the default notification sound when checked.

#### Vibrate

Vibrates when checked.

#### Flash LED

Flash the notification LED using the supplied color and blink rate. Notification LED and user defined colors are not supported on all devices.

#### Local only

Whether it's recommended to show this notification only on the main device but not on paired devices like an Android Wear watch.

#### Accent color

The color used by the device for in the notification (usually the background color of the icon in the expanded statusbar).

#### Ongoing

Flags this notification as an ongoing event and prevents the removal of this notification from the statusbar. A notification ID is mandatory when this option is selected.

#### Keep on Clear

Prevents the removal of this notification from the statusbar. A notification ID is mandatory when this option is selected.

#### Notification ID

Defines the ID (a number from 1 to 999) to use as the identification of this notification. [Variables are supported.](action_script.md#string-inline-expressions)
This is useful when the notification is used for trigger **Notification on Statusbar Selected** or when the notification is used to show a profile like status.
A notification with the same ID replaces an older notification of the same ID. The notification can be removed from the statusbar using the action **Remove Notification on Statusbar**.

The button **Remove, X** can be used to remove a notification with this ID on the statusbar.

#### Category (Android 5+)

The category of the notification. The category defines if a notification is allowed to pass the interruptions filter.

#### Priority (Android 4.1+)

Defines the priority of the notification. A notification with a low priority might be displayed in the expanded statusbar only (depends on Android version).
Settings like **Play Sound** and **Vibrate** can be ignored by the system when the priority is low or forced when the priority is high.

Note: On Android 8+ the priority is mapped to notification channel importance as follows: Minimum‑>Low, Low‑>Medium, Normal‑>High, High‑>Urgent, Maximum‑>Maximum.

#### Visibility (Android 5+)

Whether notifications are secret, private or public which defines whether the notifications are displayed on the lock screen or not. The lock screen must also be configured appropriately.

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

#### Actions for Android Wear (Android 4.1+)

Up to three actions to show on an Android Wear device. When such an action is defined, the other actions are usually not displayed anymore on the Android Wear device.

Tip: Use action **Execute Flows** to execute a complex flow consisting of multiple actions and conditions.

Following variables are supplied to the executed action:

- `action_number`: contains the number of the action (1, 2 or 3)
- `action_text`: the text label of the selected action button on the notification
- `input_value`: the selected input value or the recognized text of the speech input

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
