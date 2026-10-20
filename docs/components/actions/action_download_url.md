---
title: "Action - Download URL"
source: https://automagic4android.com/action_download_url_en.html
archived: 2022-10-06
archive_url: https://web.archive.org/web/20221006134710/https://automagic4android.com/action_download_url_en.html
category: action
---

# Action - Download URL

The action **Download URL** directly downloads a file in the background to the defined directory.

Examples:

- Download a PDF newspaper every morning.

### Settings

#### URL

The URL to download. [Variables are supported.](action_script.md#string-inline-expressions)
Examples:

- `http://example.com/newspaper_{triggertime,dateformat,yyyyMMdd}.pdf` becomes `http://example.com/newspaper_20110213.pdf`

#### Directory

The directory to place the downloaded file in. [Variables are supported.](action_script.md#string-inline-expressions)

#### Filename

The filename to use for the downloaded file. The URL is used to determine the filename if none is provided. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `file_path` — the target path of the downloaded file

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
