---
title: "Action - Delete Files"
source: https://automagic4android.com/action_delete_files_en.html
archived: 2022-10-07
archive_url: https://web.archive.org/web/20221007114117/https://automagic4android.com/action_delete_files_en.html
category: action
---

# Action - Delete Files

The action **Delete Files** locally deletes one or multiple files or folders including contained files.

Examples:

- Monthly delete all files in the `/mnt/sdcard/download/` folder.

### Settings

#### Source Files

A comma separated list of files or directories to delete. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/download/*` matches all files and subfolders in the `download` directory

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
