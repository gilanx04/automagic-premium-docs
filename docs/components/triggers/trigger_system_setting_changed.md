---
title: "Trigger - System Setting Changed"
source: https://automagic4android.com/trigger_system_setting_changed_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - System Setting Changed

The trigger **System Setting Changed** is executed whenever a setting in the systems setting database was changed.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Play an alert when the system turns on the blocking mode.

### Settings

#### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global Settings valid for all users of the device (Android 4.2+)

#### Name

The name of the setting to watch. Glob patterns are supported.

#### Variable

The name of the variable with the new value of the setting to pass to the flow.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `old_setting` — the value of the setting before it was changed
- `setting` — the new value of the setting
- `setting_name` — the name of the setting that changed. Especially useful when multiple settings are watched using a glob pattern.

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
