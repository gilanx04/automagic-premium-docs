---
title: "Condition - WiFi Available"
source: https://automagic4android.com/condition_wifi_available_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - WiFi Available

The condition **WiFi Available** checks whether one specific WiFi access point is currently available. The condition waits for the first available scan result when wifi has just been enabled and no scan result is available yet.

Note: Starting with Android 6, scan results are only provided to apps when the location services of the system are enabled.

Examples:

- Check if a specific free access point is available and enable this one.

### Settings

#### SSID List

The comma separated list of SSIDs to accept. The condition is true when one of the access points in the list is available. Glob patterns can be used to match multiple SSIDs. [Variables are supported.](../actions/action_script.md#string-inline-expressions)
The variables supplied by the condition relate to the available access point with the highest signal strength.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `access_points` — the list of available access point SSIDs
- `bssid` — the BSSID of the available access point
- `bssids` — the list of BSSIDs of the available access points
- `ssid` — the SSID of the WiFi network
- `capabilities` — the capabilities of the WiFi network
- `frequency` — the frequency of the WiFi network
- `level` — the signal strength level of the WiFi network

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
