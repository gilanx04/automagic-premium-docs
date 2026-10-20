---
title: "Action - Import Flows"
source: https://automagic4android.com/action_import_flows_en.html
archived: 2024-04-19
archive_url: https://web.archive.org/web/20240419014331/https://automagic4android.com/action_import_flows_en.html
category: action
---

# Action - Import Flows

The action **Import Flows** imports all flows of the specified file. The imported flows are **disabled**. Already existing flows are not imported.
Flows can be enabled after importing when desired using action **Set Flow State** and the variable `{imported_flow_names,listformat,comma}`.

Examples:

- Import a flow to lock the device on the stolen device.

### Settings

#### File

The file to import. [Variables are supported.](action_script.md#string-inline-expressions)

#### Replace existing

Whether or not to replace existing Flows, Triggers, Actions, Conditions and Widgets with the same name.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `imported_flow_names` — the list of imported flows
- `duplicate_flow_names` — the list of duplicate flows that have not been imported

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
