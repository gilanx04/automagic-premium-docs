---
title: "Action - FTP Delete Files"
source: https://automagic4android.com/action_ftp_delete_files_en.html
archived: 2022-10-06
archive_url: https://web.archive.org/web/20221006132227/https://automagic4android.com/action_ftp_delete_files_en.html
category: action
---

# Action - FTP Delete Files

The action **FTP Delete Files** deletes the files specified on the FTP server.

Examples:

- Recursively delete all files in a directory on the server before uploading new files.

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

#### Paths on Server

A comma separated list of files or directories to delete on the server. Glob patterns can be used to match multiple files. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/pub/export*` matches all files with a name starting with `export` in folder `/pub`

#### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
