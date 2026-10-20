---
title: "Action - Init Variables File Info"
source: https://automagic4android.com/action_init_variables_file_info_en.html
archived: 2024-02-22
archive_url: https://web.archive.org/web/20240222114720/https://automagic4android.com/action_init_variables_file_info_en.html
category: action
---

# Action - Init Variables File Info

The action **Init Variables File Info** provides information about a file as variables to the flow.

Examples:

- Check if a file is older than one week and delete the file.

### Settings

#### File

The file to check. [Variables are supported.](action_script.md#string-inline-expressions)

#### File Type

The variable to store the file type (`dir`, `file` or `other`).

#### File Exists

Variable to store whether the file exist or not.

#### File Size

Variable to store the size of the file in bytes.

#### recursive for directory

For directories whether to collect the size of all directly contained files or to also recursively traverse and sum the size of all subdirectories.

#### File Last Modified

Variable to store the last modification timestamp.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `file_type` — the type of the file (`dir`, `file` or `other`)
- `file_exists` — if the file exist or not (`true` or `false`)
- `file_size` — size of the file in bytes (or the sum of the files in directory)
- `file_last_modified` — timestamp of the last modification

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
