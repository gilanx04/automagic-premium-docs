---
title: "Action - Input Speech (Experimental)"
source: https://automagic4android.com/action_input_speech_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Input Speech (Experimental)

The action **Input Speech (Experimental)** starts the speech recognition of the device and provides the recognized text to the flow in variable `value`. The speech recognition engine usually requires network access.

Examples:

- Control Automagic using spoken commands.

### Settings

#### UI Mode

Whether user interface should be shown or the speech recognition should be executed in the background.

#### Prompt

An optional title to show in the user interface. This setting might be ignored by the engine. [Variables are supported.](action_script.md#string-inline-expressions)

#### Language

Optional the desired language to use in the speech recognition engine. This setting might be ignored by the engine. [Variables are supported.](action_script.md#string-inline-expressions)

#### Use Bluetooth headset (Android 3+)

Whether or not a Bluetooth headset is used.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `value` — the recognized text
- `operation` — whether the recognition was successful (ok) or not (cancel)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
