---
title: "Action - Dropbox Upload File"
source: https://automagic4android.com/action_dropbox_upload_file_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001215849/https://automagic4android.com/action_dropbox_upload_file_en.html
category: action
---

# Action - Dropbox Upload File

The action **Dropbox Upload File** uploads one file to your Dropbox.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the your Dropbox.

### Settings

#### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

#### Local File

The absolute path of the local file to upload. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`

#### Path on Dropbox (including filename)

The absolute path of the file on Dropbox. The path has to include the filename of the target file. This allows you to store the file using a different name on your Dropbox. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
