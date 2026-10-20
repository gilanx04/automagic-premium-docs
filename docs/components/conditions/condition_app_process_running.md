---
title: "Condition - App Process Running"
source: https://automagic4android.com/condition_app_process_running_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - App Process Running

The condition **App Process Running** checks whether the process hosting an app is currently running.

Note: Android keeps processes in memory even when the process might not be required anymore and enough free memory is available.

Note: The official API used to access this information has been removed by Google on Android 5.1.1 which means that the condition is now marked as *not officially supported*.

Note: The unofficial workarounds to access this information don't work anymore on most devices running Android 7.

### Settings

#### Package Name

The name of the process to check. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `pid` — the id of the process
- `importance` — the importance of the process. The smaller the value the higher the importance.
- `lru` — least recently used. Smaller value means more recently used.
- `process_state` — State of the process (2=Process hosting the current top activities)
- `uid` — the user id of the process

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
