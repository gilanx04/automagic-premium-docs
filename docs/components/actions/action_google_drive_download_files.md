---
title: "Action - Google Drive Download Files (Experimental)"
source: https://automagic4android.com/action_google_drive_download_files_en.html
archived: 2024-12-08
archive_url: https://web.archive.org/web/20241208213547/https://automagic4android.com/action_google_drive_download_files_en.html
category: action
---

# Action - Google Drive Download Files (Experimental)

The action **Google Drive Download Files (Experimental)** downloads multiple files and directories recursively to your device.

Warning: This action downloads all specified files and overwrites already existing target files. The files will be downloaded even when the same file already exists on the device.

Note: Google Drive allows to create duplicate files which is not possible on a regular filesystem. Automagic only considers the newest file in such a case and ignores duplicates.
Note: Google Documents are not downloaded.

Examples:

- Download each morning the newest file of keypass containing your passwords to ensure you have the newest offline copy available.

### Settings

#### Device account

The account to access Google Drive.

#### Google Drive Paths

A comma separated list of files or directories to download from Google Drive. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

#### Target

The absolute path of the target directory to download the files to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
