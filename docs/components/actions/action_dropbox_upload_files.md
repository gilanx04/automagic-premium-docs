---
title: "Action - Dropbox Upload Files"
source: https://automagic4android.com/action_dropbox_upload_files_en.html
archived: 2024-04-20
archive_url: https://web.archive.org/web/20240420131532/https://automagic4android.com/action_dropbox_upload_files_en.html
category: action
---

# Action - Dropbox Upload Files

The action **Dropbox Upload Files** uploads one or multiple files and directories recursively to your Dropbox.

Warning: This action uploads all specified files and overwrites already existing target files. The files will be uploaded even when the same file already exists on Dropbox.

Warning: Dropbox limits the amount of data each user can transfer.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the your Dropbox.

### Settings

#### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

#### Source Files

A comma separated list of files or directories to upload to Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export*` matches all files with a name starting with `export` in folder `/mnt/sdcard`

#### Path on Dropbox

The absolute path of the target on Dropbox to upload the files to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
