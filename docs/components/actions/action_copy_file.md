---
title: "Action - Copy File"
source: https://automagic4android.com/action_copy_file_en.html
archived: 2024-04-20
archive_url: https://web.archive.org/web/20240420141410/https://automagic4android.com/action_copy_file_en.html
category: action
---

# Action - Copy File

The action **Copy File** locally copies a file.

Examples:

- Create a weekly backup of the Automagic flows to a file containing the timestamp.

### Settings

#### Source File

The absolute path of the file to copy. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`

#### Target File (including filename)

The absolute path of the target file. The path has to include the filename of the target file. [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
