---
title: "Trigger - Battery Saver Mode"
source: https://automagic4android.com/trigger_power_save_mode_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Battery Saver Mode

The trigger **Battery Saver Mode** is executed when the battery saving mode of the device is changed (Android 5+).
Warning: This function does not work for manufacturer specific battery saving modes like Samsungs (Ultra-)energy saving mode or Sony and HTC specific modes. Please use action **System Setting Changed** on such devices.

Examples:

- Turn off a few flows when the battery saver is activated.

### Settings

#### Turned On or Off

Whether to execute the flow when the mode was turned on or off.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
