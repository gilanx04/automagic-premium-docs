---
title: "Trigger - Battery Low Condition"
source: https://automagic4android.com/trigger_battery_low_okay_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Battery Low Condition

The trigger **Battery Low Condition** is executed when the battery level becomes low or when the battery level becomes OK again after it was low.

Examples:

- Lower the display brightness when the battery level becomes low.
- Turn off WiFi when the battery level becomes low.
- Turn on WiFi when the battery level becomes OK again.

### Settings

#### Battery Condition

**low**
The battery level becomes low (the exact value can differ between different devices).

**OK**
The battery level becomes OK again (the exact value can differ between different devices).

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
