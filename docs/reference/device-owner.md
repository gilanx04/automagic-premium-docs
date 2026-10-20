---
title: "Device Owner"
source: https://automagic4android.com/automagic/1.38/onlinehelp/en/device_owner.html
archived: 2019-05-17
archive_url: https://web.archive.org/web/20190517133639/https://automagic4android.com/automagic/1.38/onlinehelp/en/device_owner.html
category: reference
---

# Device Owner

Setting the device administrator of an app as a device owner enables several capabilities to an app that are not available otherwise.

The procedure to set Automagic as the device owner is quite complicated and can potentially go wrong so this feature is completely unsupported and you do this on your own risk.

1. Enable Developer options->USB debugging on your device
2. Set the Screen lock to **None**
3. Install Automagic available on Google Play
4. Remove all Google Accounts from your device
5. Execute `adb shell dpm set-device-owner ch.gridvision.ppam.androidautomagic/.AutomagicDeviceAdminReceiver`
6. Add your Google accounts

---

[← Indeks referensi](README.md) · [Peta dokumentasi](../README.md)
