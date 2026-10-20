---
title: "Action - Dropbox Init Variable File List"
source: https://automagic4android.com/action_dropbox_init_variable_file_list_en.html
archived: 2022-09-26
archive_url: https://web.archive.org/web/20220926221207/https://automagic4android.com/action_dropbox_init_variable_file_list_en.html
category: action
---

# Action - Dropbox Init Variable File List

The action **Dropbox Init Variable File List** lists the files of a directory that match the specified name pattern.

Examples:

- Get a list of files and download only the ones smaller than 1MB.

### Settings

#### Dropbox Access

Whether Dropbox access is currently possible or not and allows to sign in to your Dropbox account.

Installing the Dropbox app should not be required but can help to circumvent authentication problems on some devices.

#### Variable

The name of the variable to hold the list of files. [Variables are supported.](action_script.md#string-inline-expressions)

#### File Pattern

The files to list. The file pattern can contain glob pattern characters like `*` and `?`. [Variables are supported.](action_script.md#string-inline-expressions)

#### Include file attributes

When selected, returns for each file a list of attributes with path, file type, file size and file date.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `files` — the list of files

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
