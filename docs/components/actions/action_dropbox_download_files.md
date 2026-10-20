---
title: "Action - Dropbox Download Files"
source: https://automagic4android.com/action_dropbox_download_files_en.html
archived: 2024-04-14
archive_url: https://web.archive.org/web/20240414172817/https://automagic4android.com/action_dropbox_download_files_en.html
category: action
---

# Action - Dropbox Download Files

The action **Dropbox Download Files** downloads multiple files and directories recursively to your device.

Warning: This action downloads all specified files and overwrites already existing target files. The files will be downloaded even when the same file already exists on the device.

Warning: Dropbox limits the amount of data each user can transfer.

Examples:

- Download each morning the newest file of keypass containing your passwords to ensure you have the newest offline copy available.

### Settings

#### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

#### Dropbox Paths

A comma separated list of files or directories to download from Dropbox. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/backup/export*` matches all files with a name starting with `export` in folder `/backup`

#### Target

The absolute path of the target directory to download the files to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
