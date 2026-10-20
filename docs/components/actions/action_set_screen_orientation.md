---
title: "Action - Set Screen Orientation"
source: https://automagic4android.com/action_set_screen_orientation_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Screen Orientation

The action **Set Screen Orientation** forces the device to use the specified screen orientation setting. It can be used to force the screen to always use landscape mode or to use the sensor to enable reverse portrait and reverse landscape orientations.

Warning: This function is not officially supported by Android and might not work on all devices. Some apps like launchers or games might crash when the screen can not be changed to the rotation required by the app.

Examples:

- Force the device to use landscape mode even for the launcher.

### Settings

#### Screen Orientation

The orientation setting to force:

- **Reset to default**: Reset to device default so the orientation is determined by the system
- **Landscape**: Force landscape
- **Portrait**: Force portrait
- **Sensor**: Force the use of the sensor detected orientation, even when an app requests landscape only
- **Don't use sensor**: Don't allow the use of the sensor to determine the orientation
- **Sensor Landscape**: Landscape or reverse landscape as determined by the sensor (from Android 2.3)
- **Sensor Portrait**: Portrait or reverse portrait as determined by the sensor (from Android 2.3)
- **Reverse Landscape**: Force reverse landscape (from Android 2.3)
- **Reverse Portrait**: Force reverse portrait (from Android 2.3)
- **Sensor all orientations**: All four possible orientations as determined by the sensor (from Android 2.3)

#### Show status bar notification to reset

Shows a lock icon in the statusbar to indicate that an orientation setting is enforced. Selecting the notification resets to the default value and is the same as executing this action with *Reset to default*

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
