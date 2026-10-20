---
title: "Action - Copy Files"
source: https://automagic4android.com/action_copy_files_en.html
archived: 2022-12-03
archive_url: https://web.archive.org/web/20221203000101/https://automagic4android.com/action_copy_files_en.html
category: action
---

# Action - Copy Files

The action **Copy Files** locally copies one or a list of files to the specified target directory or file.

Examples:

- Backup all files in directory `/mnt/sdcard/xyz/` to the folder `/mnt/sdcard/xyz_backup/`.

### Settings

#### Source Files

A comma separated list of files or directories to copy. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

When multiple files are matched, the target has to be a directory. The directory will be created when it does not exist yet.
A directory with an ending slash (like `/mnt/sdcard/`) matches the files contained in the directory like using `/mnt/sdcard/*`.

#### Target

The absolute path of the target file or directory. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
