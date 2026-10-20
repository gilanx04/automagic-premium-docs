---
title: "Action - Init Variable System Setting (Android Wear)"
source: https://automagic4android.com/action_init_variable_system_setting_wear_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071058/https://automagic4android.com/action_init_variable_system_setting_wear_en.html
category: action
---

# Action - Init Variable System Setting (Android Wear)

The action **Init Variable System Setting (Android Wear)** reads a value from the system setting database and stores the value in a variable.

### Settings

#### Android Wear device

The target device. [Variables are supported.](action_script.md#string-inline-expressions)

#### Category

- **System**: for regular settings
- **Secure**: for settings which can usually not be modified
- **Global**: for global Settings valid for all users of the device (Android 4.2+)

#### Name

The name of the setting to read. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable

The name of the variable to store the value in. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `setting` — the value of the setting

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
