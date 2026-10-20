---
title: "Action - Set LineageOS System Setting"
source: https://automagic4android.com/action_set_lineage_system_setting_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set LineageOS System Setting

The action **Set LineageOS System Setting** stores the specified value in the settings database of the system.

Warning: Modifying system settings to unsupported values can possibly harm your device or crash the system. Use at your own risk!

Note: Changes to some settings are not immediately picked up by the system but require an additional event to occur like turning the screen off and back on. Some settings need to be changed by special APIs, changing the value of such settings in the settings database are ignored by the system.

Note: `adb` can be used on some versions of Android to grant the permissions to modify settings from category **secure** and **global** without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic lineageos.permission.WRITE_SECURE_SETTINGS`

Examples:

- Change the value of a ROM specific setting not available in a regular action in Automagic.

### Settings

#### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global settings valid for all users of the device

#### Name

The name of the setting to modify. [Variables are supported.](action_script.md#string-inline-expressions)

#### Value

The value to store in the system settings database. [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
