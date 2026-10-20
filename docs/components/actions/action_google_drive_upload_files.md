---
title: "Action - Google Drive Upload Files (Experimental)"
source: https://automagic4android.com/action_google_drive_upload_files_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071057/https://automagic4android.com/action_google_drive_upload_files_en.html
category: action
---

# Action - Google Drive Upload Files (Experimental)

The action **Google Drive Upload Files (Experimental)** uploads one or multiple files and directories recursively to your Google Drive.

Warning: This action uploads all specified files and overwrites already existing target files.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the Google Drive.

### Settings

#### Device account

The account to access Google Drive.

#### Source Files

A comma separated list of files or directories to upload to Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

#### Path on Google Drive

The absolute path of the target on Google Drive to upload the files to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
