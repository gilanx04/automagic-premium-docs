---
title: "Action - Set Battery Saver Mode"
source: https://automagic4android.com/action_set_power_save_mode_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Battery Saver Mode

The action **Set Battery Saver Mode** turns on the battery saver mode of the device (Android 5+). Battery saver mode can not be enabled when the device is charging.

Warning: This function does not work for manufacturer specific battery saving modes like Samsungs (Ultra-)energy saving mode or Sony and HTC specific modes. Please use action **Set System Setting** on such devices.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn on the battery saver at night when no charging adapter is available.

### Settings

#### Battery Saver

Whether to turn the battery saver mode on or off.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
