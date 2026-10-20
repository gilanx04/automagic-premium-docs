---
title: "Condition - WiFi Signal Level"
source: https://automagic4android.com/condition_wifi_signal_level_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - WiFi Signal Level

The condition **WiFi Signal Level** checks the signal level of the connected wifi network.

Note: The current signal strength has to be measured using a wifi scan when the display is turned off. A wifi scan can take a few seconds and increases battery consumption.

### Settings

#### Signal Level Condition

Defines the condition that must be met to continue the flow on the true branch:

**lower than**
true when the reported level by the system is below the defined level

**higher than**
true when the reported level by the system is above the defined level

**exactly**
true when the reported level by the system is exactly on the defined level

#### Signal Level

Defines the level to compare (usually in range 0-4).

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `rssi` — the signal strength in dBm
- `signal_strength_level` — the signal strength mapped to levels (usually in range 0-4)

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
