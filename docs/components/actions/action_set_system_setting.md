---
title: "Action - Set System Setting"
source: https://automagic4android.com/action_set_system_setting_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set System Setting

The action **Set System Setting** stores the specified value in the settings database of the system.

Warning: Modifying system settings to unsupported values can possibly harm your device or crash the system. Use at your own risk!

Note: Changes to some settings are not immediately picked up by the system but require an additional event to occur like turning the screen off and back on. Some settings need to be changed by special APIs, changing the value of such settings in the settings database are ignored by the system.

Note: `adb` can be used on some versions of Android to grant the permissions to modify settings from category **secure** and **global** without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Change the value of a ROM specific setting not available in a regular action in Automagic.

### Settings working on different devices (not available on all devices)

#### Pulse notification light/LED

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `notification_light_pulse` |
| Value: | `0` = off `1` = on |

#### Night mode (Android 7+, when activated in System UI tuner)

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Secure` |
| Name: | `twilight_mode` |
| Value: | `0` = off `1` = on `2` = automatic |

#### Location mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Secure` |
| Name: | `location_mode` |
| Value: | `0` = location mode off `1` = Device only `2` = Battery saving `3` = High accuracy |

Alternatively:

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Secure` |
| Name: | `location_providers_allowed` |
| Value: | `+gps` = turn GPS on `-gps` = turn GPS off `+network` = turn Network on `-network` = turn Network off |
| Warning: Only change one value at a time! Changing multiple values at once will result in an inconsistent setting value which can only be fixed by a factory reset. | |

#### Mobile data

| Column 1 | Column 2 |
| --- | --- |
| Category: | `Global` |
| Name: | `mobile_data` |
| Value: | `0` = mobile data off `1` = mobile data on |

### LG specific settings (not available on all devices)

#### Pulse notification light/LED

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `lge_notification_light_pulse` |
| Value: | `0` = off `1` = on |

### Samsung S3 specific settings (not available on all devices)

#### Driving mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `driving_mode_on` |
| Value: | `0` = off `1` = on |

#### Power saving mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `psm_switch` |
| Value: | `0` = off `1` = on |

#### Blocking mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `dormant_switch_onoff` |
| Value: | `0` = off `1` = on |

#### Multi window mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `multi_window_enabled` |
| Value: | `0` = off `1` = on |

#### S Beam mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `sbeam_mode` |
| Value: | `0` = off `1` = on |

#### Vibration intensity

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `VIB_RECVCALL_MAGNITUDE` `VIB_NOTIFICATION_MAGNITUDE` `VIB_FEEDBACK_MAGNITUDE` |
| Value: | `0` = weak to `5` = strong |

### Samsung S5 specific settings (not available on all devices)

#### Car mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `car_mode_on` |
| Value: | `0` = off `1` = on |

#### Power saving mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `powersaving_switch` |
| Value: | `0` = off `1` = on |

#### Blocking mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `dormant_switch_onoff` |
| Value: | `0` = off `1` = on |

#### Multi window mode

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `multi_window_enabled` |
| Value: | `0` = off `1` = on |

#### Toolbox

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `toolbox_onoff` |
| Value: | `0` = off `1` = on |

#### Smart stay

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `intelligent_sleep_mode` |
| Value: | `0` = off `1` = on |

#### Smart pause

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `smart_pause` |
| Value: | `0` = off `1` = on |

#### Touch sensitivity

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `auto_adjust_touch` |
| Value: | `0` = off `1` = on |

#### Vibration intensity

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `VIB_RECVCALL_MAGNITUDE` `VIB_NOTIFICATION_MAGNITUDE` `VIB_FEEDBACK_MAGNITUDE` |
| Value: | `0` = weak to `5` = strong |

### CyanogenMod specific settings (not available on all devices)

#### Expanded desktop

| Column 1 | Column 2 |
| --- | --- |
| Category: | `System` |
| Name: | `expanded_desktop_state` |
| Value: | `0` = off `1` = on |

### Settings

#### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global settings valid for all users of the device (Android 4.2+)

#### Name

The name of the setting to modify. [Variables are supported.](action_script.md#string-inline-expressions)

#### Value

The value to store in the system settings database. [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
