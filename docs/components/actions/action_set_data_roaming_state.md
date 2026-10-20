---
title: "Action - Set Data Roaming State"
source: https://automagic4android.com/action_set_data_roaming_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Data Roaming State

The action **Set Data Roaming State** turns the global data roaming setting on or off.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Example:

- Activate data roaming abroad every morning for 10 minutes to synchronize the mails and deactivate data roaming again for the rest of the day.

### Settings

#### Data Roaming

Whether to turn data roaming on or off.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
