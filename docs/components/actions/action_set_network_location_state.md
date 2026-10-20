---
title: "Action - Set Network Location State"
source: https://automagic4android.com/action_set_network_location_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Network Location State

The action **Set Network Location State** changes the setting whether the system can use WiFi access points and the mobile network to determine your location.

Note: Android shows a confirmation dialog on some devices.
Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn on the network location when Google Maps is started.

### Settings

#### Network Location

Whether the network location provider can be used to determine the location.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
