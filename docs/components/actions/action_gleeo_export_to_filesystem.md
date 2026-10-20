---
title: "Action - Gleeo Filesystem Export"
source: https://automagic4android.com/action_gleeo_export_to_filesystem_en.html
archived: 2022-12-03
archive_url: https://web.archive.org/web/20221203001218/https://automagic4android.com/action_gleeo_export_to_filesystem_en.html
category: action
---

# Action - Gleeo Filesystem Export

The action **Gleeo Filesystem Export** creates a CSV export of the defined projects and time range.

Examples:

- Backup all data in Gleeo Time Tracker to the SD card.
- Export the current month by pressing a shortcut on the launcher and attach the created file to a Google Mail message draft.
- Each month export all recorded entries of the month to the SD card and send the file by mail to your employer.

### Settings

#### Domains to Export

The list of domains to export. [Variables are supported.](action_script.md#string-inline-expressions)

#### Projects to Export

The list of projects to export. [Variables are supported.](action_script.md#string-inline-expressions)

#### Tasks to Export

The list of tasks to export. [Variables are supported.](action_script.md#string-inline-expressions)

#### Time Range

The time range to export.

#### CSV Column Delimiter

The delimiter used to separate two columns. Excel users can set this to `Semicolon` to simplify the import in Excel.

#### Target File

The file to store the exported data in. Variables can be used to create dynamic file names based on time.

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`
- `/mnt/sdcard/export_{export_start_time,dateformat,yyyy_MM_dd}-{export_end_time,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_03_01-2011_03_31.csv`

#### Encoding

The encoding used to save the file.

#### Attach to Mail

Opens the desired Mail App and attaches the CSV file.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `export_start_time` — the start time of the exported time range
- `export_end_time` — the end time of the exported time range
- `export_path` — the absolute path of the exported file

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
