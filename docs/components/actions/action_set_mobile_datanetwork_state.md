---
title: "Action - Set Mobile Datanetwork State"
source: https://automagic4android.com/action_set_mobile_datanetwork_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Mobile Datanetwork State

The action **Set Mobile Datanetwork State** turns the mobile datanetwork on or off.

Warning: This function is not officially supported by Android and might not work on all devices.

Warning: This function requires root access on some devices.

Note: `adb` can be used on some versions of Android to grant the permissions to execute the action without root:

1. Install `adb` on a computer ([search internet on how to install adb](https://www.google.com/search?q=install+adb+for+android))
2. enable **USB Debugging** in **System settings** -> **Developer options** on your Android device
3. connect your Android device to the computer
4. execute following command in a terminal: `adb shell pm grant ch.gridvision.ppam.androidautomagic android.permission.WRITE_SECURE_SETTINGS`

Examples:

- Turn the mobile datanetwork off at night.

### Settings

#### Mobile Datanetwork

Whether to turn mobile datanetwork on or off.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
