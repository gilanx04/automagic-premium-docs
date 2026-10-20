---
title: "Action - FTP Upload File"
source: https://automagic4android.com/action_ftp_upload_file_en.html
archived: 2024-04-20
archive_url: https://web.archive.org/web/20240420131232/https://automagic4android.com/action_ftp_upload_file_en.html
category: action
---

# Action - FTP Upload File

The action **FTP Upload File** uploads one file to an FTP server.

Examples:

- Upload a backup of all data in Gleeo Time Tracker to the your company server.

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

#### Local File

The absolute path of the local file to upload. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `/mnt/sdcard/export_{triggertime,dateformat,yyyy_MM_dd}.csv` becomes `/mnt/sdcard/export_2011_02_13.csv`

#### Path on Server (including filename)

The absolute path of the file on the FTP server. The path has to include the filename of the target file. This allows you to store the file using a different name on your server. [Variables are supported.](action_script.md#string-inline-expressions)

#### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](action_script.md#string-inline-expressions)

#### Show progress notification

Whether or not to show a notification on the statusbar indicating the progress of the operation.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
