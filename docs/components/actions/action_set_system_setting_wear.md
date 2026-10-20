---
title: "Action - Set System Setting (Android Wear)"
source: https://automagic4android.com/action_set_system_setting_wear_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set System Setting (Android Wear)

The action **Set System Setting (Android Wear)** stores the specified value in the settings database of the system.

Warning: Modifying system settings to unsupported values can possibly harm your device or crash the system. Use at your own risk!

Note: Changes to some settings are not immediately picked up by the system but require an addition event to occur like turning the screen off and back on. Some settings need to be changed by special APIs, changing the value of such settings in the settings database are ignored by the system.

Examples:

- Change the value of a ROM specific setting not available in a regular action in Automagic.

### Settings

#### Android Wear device

The target device. [Variables are supported.](action_script.md#string-inline-expressions)

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
