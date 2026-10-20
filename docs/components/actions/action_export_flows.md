---
title: "Action - Export Flows"
source: https://automagic4android.com/action_export_flows_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071059/https://automagic4android.com/action_export_flows_en.html
category: action
---

# Action - Export Flows

The action **Export Flows** exports the selected flows to the specified file.

Examples:

- Export all flows to a file and upload the file to Dropbox as a backup.

### Settings

#### Flow pattern list

A comma separated list of flow names to export. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*time tracking*`

#### Exclude flow pattern list

A comma separated list of flow names to **not** export even when the field **Flow pattern list** includes the flow. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](action_script.md#string-inline-expressions)

#### Widget pattern list

A comma separated list of widget names to export. Glob patterns `*` and `?` can be used to match similar named widgets. [Variables are supported.](action_script.md#string-inline-expressions)

#### Exclude widget pattern list

A comma separated list of widget names to **not** export even when the field **Widget pattern list** includes the widget. Glob patterns `*` and `?` can be used to match similar named widgets. [Variables are supported.](action_script.md#string-inline-expressions)

#### Target File

The path of the target file. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `export_path` — the path of the created file

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
