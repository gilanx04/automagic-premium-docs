---
title: "Action - FTP Init Variable File List"
source: https://automagic4android.com/action_ftp_init_variable_file_list_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001211903/https://automagic4android.com/action_ftp_init_variable_file_list_en.html
category: action
---

# Action - FTP Init Variable File List

The action **FTP Init Variable File List** lists the files of a directory that match the specified name pattern.

Examples:

- Get a list of files and download only the ones smaller than 1MB.

### Settings

#### Protocol

Whether to use regular FTP (unencrypted), FTPS (Implicit FTP over SSL/TLS, default port 990) or FTPES (Explicit FTP over SSL/TLS).

#### Data Channel Protection (only for FTPS and FTPES)

Whether data transferred on the data channel should be encrypted (P) or not (C).

#### Server/Port

The name or IP and port (default 21) of the FTP server. [Variables are supported.](action_script.md#string-inline-expressions)

#### Username

The username to connect. [Variables are supported.](action_script.md#string-inline-expressions)

#### Password

The password to connect. [Variables are supported.](action_script.md#string-inline-expressions)

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
