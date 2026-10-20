---
title: "Trigger - Volume Long Press Event"
source: https://automagic4android.com/trigger_volume_long_press_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Volume Long Press Event

The trigger **Volume Long Press Event** is executed when one of the volume keys is pressed down for a longer duration or hold and then released.

Note: `adb` has to be used to grant a permission to Automagic to use this feature:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.SET_VOLUME_KEY_LONG_PRESS_LISTENER`

Warning: This function is not officially supported by Android and might not work on all devices.
Warning: Activating this trigger prevents that holding the volume button for a longer duration changes the volume.
Warning: This trigger can miss Up events in case an app or dialog is shown while the volume key is held down.
Examples:

- Hold the volume down key pressed to skip to the next song.

### Settings

#### Keys

The list of names of keys that should execute the trigger. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Press Duration

The minimum amount of time that the key has to be hold to execute the trigger. The Down action will be executed when the specified duration is reached, the up action as soon as the key is released.

#### Actions

Whether down, up or both actions should execute the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `key_code` — the numeric keycode
- `key_code_name` — the name of the keycode
- `key_duration` — the duration of the event in milliseconds
- `key_source_device_id` — the ID of the sending device
- `key_action_down` — whether the action was down
- `key_action_up` — whether the action was up

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
