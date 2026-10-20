---
title: "Action - FTP Create Directories"
source: https://automagic4android.com/action_ftp_create_directories_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001203532/https://automagic4android.com/action_ftp_create_directories_en.html
category: action
---

# Action - FTP Create Directories

The action **FTP Create Directories** creates one or multiple directories on an FTP server.

Examples:

- create a directory before files are uploaded.

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

#### Server Directories

A comma separated list of directories to create. [Variables are supported.](action_script.md#string-inline-expressions)

#### Control Encoding

Whether to use a special encoding for the control channel or not (Encoding of file names, not the encoding of the content of text files). [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
