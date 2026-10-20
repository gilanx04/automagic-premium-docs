---
title: "Action - Set Screen Brightness"
source: https://automagic4android.com/action_set_screen_brightness_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Screen Brightness

The action **Set Screen Brightness** changes the screen brightness.

Examples:

- Turn down the screen brightness when the battery is below 50%.
- Turn the screen brightness to maximum when the power adapter is connected.

### Settings

#### Automatic brightness

Whether to use automatic brightness or the value specified using the slider. [Variables are supported.](action_script.md#string-inline-expressions)

#### Adaptive brightness

Whether adaptive brightness should be changed to the defined value. [Variables are supported.](action_script.md#string-inline-expressions)

Warning: This function is not officially supported by Android and might not work on all devices.

#### Force update

Whether it should be ensured that the system applies the new values immediately. Otherwise the changes might take effect when the screen is turned on the next time on some versions of Android. Disabling this option can avoid flickering on some devices.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
