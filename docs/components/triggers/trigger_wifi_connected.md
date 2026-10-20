---
title: "Trigger - WiFi Connected"
source: https://automagic4android.com/trigger_wifi_connected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - WiFi Connected

The trigger **WiFi Connected** is executed when a connection with the defined network has been established.

Examples:

- Download a file as soon as WiFi is available.

### Settings

#### SSID List

The list of SSIDs to execute the flow when connected. The list can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Trigger on BSSID changes

Whether to execute the trigger when the BSSID changes (change of the accesspoint within the same SSID).

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `bssid` — the BSSID of the connected WiFi network
- `ssid` — the SSID of the connected WiFi network

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
