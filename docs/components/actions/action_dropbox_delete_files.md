---
title: "Action - Dropbox Delete Files"
source: https://automagic4android.com/action_dropbox_delete_files_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001203655/https://automagic4android.com/action_dropbox_delete_files_en.html
category: action
---

# Action - Dropbox Delete Files

The action **Dropbox Delete Files** deletes the defined files on Dropbox.

Examples:

- Delete all files in a folder before uploading new files to this folder to get rid of files you don't need anymore.

### Settings

#### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

#### Dropbox Paths

A comma separated list of files or directories to delete on Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
