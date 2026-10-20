---
title: "Trigger - WiFi State"
source: https://automagic4android.com/trigger_wifi_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - WiFi State

The trigger **WiFi State** is executed when the devices wireless network adapter changes to one of the defined states.

Examples:

- Enable some download flows when WiFi is turned on.

### Settings

#### WiFi States

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_wifi_state` — the wifi state (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=unknown)
- `wifi_state` — the wifi state (0=disabling, 1=disabled, 2=enabling, 3=enabled, 4=unknown)

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
