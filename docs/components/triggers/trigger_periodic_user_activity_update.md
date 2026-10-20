---
title: "Trigger - User Activity (Experimental)"
source: https://automagic4android.com/trigger_periodic_user_activity_update_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - User Activity (Experimental)

The trigger **User Activity (Experimental)** asks the device to periodically check most probably physical activity of the user like driving a car, riding a bike or walking.

Note: The detection of the current activity is a feature of the device provided by Google. Automagic can not change or improve the quality of the detected activity.

Examples:

- Check the activity every 5 minutes to measure how much time the user walks per day and how much time the user sits in the office.
- Increase the ringer volume when the user is driving in a car.

### Settings

#### Trigger when

- **Activity detected**: execute the flow when the defined activity begins or ends.
- **Periodically**: execute the flow periodically even when the activity stays the same.

#### Activity

Defines which activity should trigger the flow. **Begin** executes the flow when the detected activity switches to the defined activity and was different before. **Ends** executed the flow when the defined activity was in progress before and is not detected anymore.

#### Enforce Exact Frequency

Ensures that the flow is executed exactly at the defined frequency even when the detected activity changes more or less frequent.

#### Check Frequency

The desired time between activity checks. The actual time between activity updates depends on the device when **Enforce Exact Frequency** is not checked.
The device can detect the activity more frequently when another app is interested in activity updates and uses a shorter update interval. Some devices turn off activity detection when activity `still` is detected and a low power sensor to detect device movement is available.

#### Minimum Confidence

The minimum confidence level to accept (0=unconfident, 100=confident).

#### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

#### Weekdays

The day on which the trigger should be active.

#### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

#### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../../reference/device-idle-mode.md))

#### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `activity_name` — the name of the activity ("in\_vehicle", "on\_bicycle", "on\_foot", "still", "unknown", "tilting", "walking", "running")
- `activity_type` — the type of the activity as a number (0=in\_vehicle, 1=on\_bicycle, 2=on\_foot, 3=still, 4=unknown, 5=tilting, 7=walking, 8=running)
- `activity_confidence` — the confidence in a number from between 0=unconfident and 100=confident
- `activity_time` — the time when the activity was originally detected
- `detected_activities` — list of detected activities sorted by confidence (descending). Each item is a map containing activity\_name, activity\_type, activity\_confidence.

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
