---
title: "Action - Move Files"
source: https://automagic4android.com/action_move_files_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Move Files

The action **Move Files** locally moves one or a list of files to the specified target directory or file.
A move is implemented to use a `rename` operation when possible. If a `rename` is not possible, the file/folder is copied to the target directory and afterwards the source is deleted.

Examples:

- Move all files in directory `/mnt/sdcard/xyz/` to the folder `/mnt/sdcard/xyz_backup/`.
- Rename directory `/mnt/sdcard/xyz` to `/mnt/sdcard/xyz_backup`.

### Settings

#### Source Files

A comma separated list of files or directories to move. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

When multiple files are matched the target has to be a directory. The directory will be created when it does not exist yet.
A directory with an ending slash (like `/mnt/sdcard/`) matches the files contained in the directory like using `/mnt/sdcard/*`.

#### Target

The absolute path of the target file or directory. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
