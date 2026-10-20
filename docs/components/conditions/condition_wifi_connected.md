---
title: "Condition - WiFi Connected"
source: https://automagic4android.com/condition_wifi_connected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - WiFi Connected

The condition **WiFi Connected** checks whether the device is currently connected to one of the specified WiFi networks.

Examples:

- Start recording in **Gleeo Time Tracker** when you are in the office and connected to the wireless network.
- Enable a flow downloading big PDF files only when connected to your free wireless network at home.

### Settings

#### SSID List

The comma separated list of SSIDs to accept. Glob patterns can be used to match multiple SSIDs. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `bssid` — the BSSID of the connected WiFi network
- `ssid` — the SSID of the connected WiFi network

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
