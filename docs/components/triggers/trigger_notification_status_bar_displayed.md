---
title: "Trigger - Notification on Statusbar Displayed"
source: https://automagic4android.com/trigger_notification_status_bar_displayed_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Notification on Statusbar Displayed

The trigger **Notification on Statusbar Displayed** is executed when a notification is displayed in the statusbar.

Examples:

- Turn the screen on when Gmail app receives a mail.

### Settings

#### Package Name

The comma separated list of apps that displayed the notification. Glob patterns can be used to match multiple packages.

#### Filter

Defines the text that must be contained in one of the available fields.

#### Ignore regular events

Defines whether or not the trigger should execute the flow for regular events.
A notification is considered *regular* when the notification is not marked as ongoing by the posting app.

#### Ignore ongoing events

Defines whether or not the trigger should execute the flow for ongoing events.
A notification is marked as an ongoing event by the application that posts the notification and is usually set when a notification shows some progress like a file download, an app is playing a sound, or an app is running as a foreground service.

#### Ignore group summary

Defines whether or not the trigger should execute the flow for group summaries.
A group summary is an additional notification that is used to group several related notifications together.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `title` — the title of the displayed notification
- `content_title` — the title of the content displayed by the notification
- `content_title_big` — the title of the big content displayed by the notification
- `notification_text` — the textual content of the notification
- `notification_text_big` — the textual content of the big, expanded view of the notification
- `notification_channel_id` — the ID of the notification channel
- `notification_priority` — the priority of the notification (-2=Minimum to 2=Maximum), when available
- `notification_large_icon` — the large icon of the notification, when available
- `notification_when` — the time shown in the notification
- `notification_number` — number shown in the notification, when available
- `notification_vibrate_default` — whether the notification vibrates using the default pattern
- `notification_vibrate_pattern` — vibration pattern as a list of numbers (pause duration in ms, vibrate duration in ms, ...), when available
- `notification_sound_default` — whether the notification should play the default notification sound
- `notification_sound_uri` — the URI of the sound to play, when available
- `notification_people` — a list of relevant people of the notification (list of URIs), when available
- `notification_info_text` — the info text displayed by the notification, when available
- `notification_sub_text` — the sub text displayed by the notification, when available
- `notification_summary_text` — the summary text displayed by the notification, when available
- `notification_progress` — the current progress shown by the notification, when available
- `notification_progress_max` — the maximum progress, when available
- `notification_progress_indeterminate` — whether the progress is indeterminate, when available
- `notification_text_lines` — the text lines shown by the notification, when available
- `notification_background_image_uri` — the URI of the background image to show, when available
- `notification_category` — the category of the notification, when available
- `notification_accent_color` — the accent color of the notification, when available
- `notification_ticker_text` — the scrolling text shown by the notification
- `notification_visibility` — the visibility of the notification (-1=secret, 0=private, 1=public)
- `notification_ongoing` — whether this is an ongoing event
- `notification_foreground_service` — whether this notification is used to mark a foreground service
- `notification_local_only` — whether the notification should be displayed on the local device only
- `notification_group` — the group key of the notification
- `notification_is_group_summary` — whether the notification is the group summary
- `package_name` — the name of the package that displayed the notification
- `app_name` — the display name of the app
- `id` — the id of the notification
- `buttons` — the list of buttons available on the big, expanded notification
- `wearable_actions` — the list of actions displayed on Android Wear

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
