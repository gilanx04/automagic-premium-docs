---
title: "Action - Init Variable Notifications on Statusbar"
source: https://automagic4android.com/action_init_variable_notifications_status_bar_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071056/https://automagic4android.com/action_init_variable_notifications_status_bar_en.html
category: action
---

# Action - Init Variable Notifications on Statusbar

The action **Init Variable Notifications on Statusbar** stores all currently shown notifications as a list in a variable.

Examples:

- Send the texts of all shown notifications by mail to your account when you receive an SMS with the text *get notifications*.

### Settings

#### Variable

The name of the variable to store the list of notifications.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `notifications` —
  the list of all notifications with a map containing following keys for each notification:

  `title`

  the title of the displayed notification

  `content_title`

  the title of the content displayed by the notification

  `content_title_big`

  the title of the big content displayed by the notification

  `notification_text` (This function is not officially supported by Android and does not work with all notifications)

  the textual content of the notification

  `notification_text_big` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the textual content of the big, expanded view of the notification

  `notification_channel_id` (Android 8.0+)

  the ID of the notification channel

  `notification_priority` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the priority of the notification (-2=Minimum to 2=Maximum), when available

  `notification_large_icon` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the large icon of the notification, when available

  `notification_when`

  the time shown in the notification

  `notification_number`

  number shown in the notification, when available

  `notification_vibrate_default`

  whether the notification vibrates using the default pattern

  `notification_vibrate_pattern`

  vibration pattern as a list of numbers (pause duration in ms, vibrate duration in ms, ...), when available

  `notification_sound_default`

  whether the notification should play the default notification sound

  `notification_sound_uri`

  the URI of the sound to play, when available

  `notification_people` (Android 4.4+)

  a list of relevant people of the notification (list of URIs), when available

  `notification_info_text` (Android 4.4+)

  the info text displayed by the notification, when available

  `notification_sub_text` (Android 4.4+)

  the sub text displayed by the notification, when available

  `notification_summary_text` (Android 4.4+)

  the summary text displayed by the notification, when available

  `notification_progress` (Android 4.4+)

  the current progress shown by the notification, when available

  `notification_progress_max` (Android 4.4+)

  the maximum progress, when available

  `notification_progress_indeterminate` (Android 4.4+)

  whether the progress is indeterminate, when available

  `notification_text_lines` (Android 4.4+)

  the text lines shown by the notification, when available

  `notification_background_image_uri` (Android 5+)

  the URI of the background image to show, when available

  `notification_category` (Android 5+)

  the category of the notification, when available

  `notification_accent_color` (Android 5+)

  the accent color of the notification, when available

  `notification_ticker_text`

  the scrolling text shown by the notification

  `notification_visibility` (Android 5+)

  the visibility of the notification (-1=secret, 0=private, 1=public)

  `notification_ongoing`

  whether this is an ongoing event

  `notification_foreground_service`

  whether this notification is used to mark a foreground service

  `notification_local_only`

  whether the notification should be displayed on the local device only

  `notification_group` (Android 7+)

  the group key of the notification

  `notification_is_group_summary` (Android 7+)

  whether the notification is the group summary

  `package_name`

  the name of the package that displayed the notification

  `app_name`

  the display name of the app

  `id` (Android 4.3+)

  the id of the notification

  `buttons` (Android 4.1+, This function is not officially supported by Android and does not work with all notifications)

  the list of buttons available on the big, expanded notification

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
