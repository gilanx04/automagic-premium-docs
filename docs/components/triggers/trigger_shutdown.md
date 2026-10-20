---
title: "Trigger - Shutdown"
source: https://automagic4android.com/trigger_shutdown_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Shutdown

The trigger **Shutdown** is executed before the device shutdown.
A flow is executed on a best effort basis, Automagic might not have enough time to execute the flow completely or some services or interfaces might already be unavailable when the shutdown is detected.

Examples:

- Vibrate before the device shuts down.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
