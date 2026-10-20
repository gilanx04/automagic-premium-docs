---
title: "Action - Google Drive Delete Files (Experimental)"
source: https://automagic4android.com/action_google_drive_delete_files_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071057/https://automagic4android.com/action_google_drive_delete_files_en.html
category: action
---

# Action - Google Drive Delete Files (Experimental)

The action **Google Drive Delete Files (Experimental)** deletes the defined files on Dropbox.

Examples:

- Delete all files in a folder before uploading new files to this folder to get rid of files you don't need anymore.

### Settings

#### Device account

The account to access Google Drive.

#### Google Drive Paths

A comma separated list of files or directories to delete on Google Drive. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
