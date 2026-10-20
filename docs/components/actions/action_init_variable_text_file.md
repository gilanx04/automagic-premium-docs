---
title: "Action - Init Variable Text File"
source: https://automagic4android.com/action_init_variable_text_file_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001195233/https://automagic4android.com/action_init_variable_text_file_en.html
category: action
---

# Action - Init Variable Text File

The action **Init Variable Text File** reads the contents of a text file into the specified variable. Files up to 1MB are supported. Binary files are not supported.

Examples:

- Read a text file containing a mail template and send the text by mail.

### Settings

#### File

The path of the file to load. [Variables are supported.](action_script.md#string-inline-expressions)

#### Encoding

The encoding used to decode the bytes of the file to text.

#### Variable

The name of the variable to store the text in. [Variables are supported.](action_script.md#string-inline-expressions)

#### Strip BOM

Whether the BOM (byte order mark) potentially found at the beginning of UTF encoded file should be removed from the resulting string or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `file_text` — the name of the variable to store the text in

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
