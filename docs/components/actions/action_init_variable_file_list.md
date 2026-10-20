---
title: "Action - Init Variable File List"
source: https://automagic4android.com/action_init_variable_file_list_en.html
archived: 2024-04-20
archive_url: https://web.archive.org/web/20240420140304/https://automagic4android.com/action_init_variable_file_list_en.html
category: action
---

# Action - Init Variable File List

The action **Init Variable File List** lists all files or only the newly added files in a directory and stores the list in a variable.

Examples:

- Send all files of a directory by mail to your mail account.
- Send all new backup files of **Gleeo Time Tracker** to your inbox.

### Settings

#### Variable

The name of the variable to hold the list of files.

#### File Pattern

The files to list. The file pattern can contain glob pattern characters like `*` and `?`.

Examples:

- `/mnt/sdcard/folder/*`
- `/mnt/sdcard/GTT-export-20120101.csv`
- `/mnt/sdcard/GTT-export-*.csv`
- `/mnt/sdcard/file1,/mnt/sdcard/file2,/mnt/sdcard/file3`

#### Include changes only

Whether to store all files matching the pattern specified in **File Pattern** or only the new files.
A file is considered to be new when it was not available the last time this action executed or the size of the file changed or the last modified time of the file has changed since the last execution of this action.

#### Include file attributes

When selected, returns for each file a list of attributes with path, file type, file size and file date.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `files` — the list of files

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
