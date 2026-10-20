---
title: "Trigger - WiFi Disconnected"
source: https://automagic4android.com/trigger_wifi_disconnected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - WiFi Disconnected

The trigger **WiFi Disconnected** is executed when a connection with the defined network has been separated.

Examples:

- Play an alert when WiFi is not available anymore.
- Turn off flows causing big data transfers.

### Settings

#### SSID List

The list of SSIDs to execute the flow when disconnected. The list can contain glob pattern characters like `*` and `?`. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `bssid` — the BSSID of the disconnected WiFi network
- `ssid` — the SSID of the disconnected WiFi network

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
