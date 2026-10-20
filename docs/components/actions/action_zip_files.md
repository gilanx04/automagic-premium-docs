---
title: "Action - Zip Files"
source: https://automagic4android.com/action_zip_files_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Zip Files

The action **Zip Files** creates a Zip archive containing the specified files and directories.

Examples:

- Zip all files in directory `/mnt/sdcard/xyz/` to the zip file `/mnt/sdcard/backup.zip`.

### Settings

#### Source Files

A comma separated list of files or directories to zip. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

The files in the ZIP file are stored relative based on the parent directory of the files to archive:

- Source Files `/mnt/sdcard/export*` will store all export\* files directly (without parent folder) in the ZIP file
- Source Files `/mnt/sdcard/download/` (note the trailing slash) will store all files in folder download directly (without parent folder) in the ZIP file
- Source Files `/mnt/sdcard/download` (no trailing slash) will store the folder `download` and its contained files in the ZIP file

#### ZIP File

The absolute path of the target ZIP file to create. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
