---
title: "Action - Kill App Process"
source: https://automagic4android.com/action_kill_app_process_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Kill App Process

The action **Kill App Process** sends the defined signal to the process using the `kill` command.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- Kill the browser app when another app is started to reclaim memory.

### Settings

#### Package Name

The name of the package to kill. [Variables are supported.](action_script.md#string-inline-expressions)

#### Signal

The signal to send.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `pid` — the id of the process
- `importance` — the importance of the process. The smaller the value the higher the importance.
- `lru` — least recently used. Smaller value means more recently used.
- `uid` — the user id of the process

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
