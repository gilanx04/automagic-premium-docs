---
title: "Action - Set Flow State"
source: https://automagic4android.com/action_set_flow_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Flow State

The action **Set Flow State** enables or disables one or many flows.

Examples:

- Disable all flows using networking features when you are roaming.
- Disable all time tracking flows on Saturday and Sunday.

### Settings

#### Flow pattern list

A comma separated list of flow names to enable or disable. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*time tracking*`

#### Exclude flow pattern list

A comma separated list of flow names to **not** affect even when the field **Flow pattern list** includes the flow. Glob patterns `*` and `?` can be used to match similar named flows. [Variables are supported.](action_script.md#string-inline-expressions)

#### Enable or disable flows

Whether to enable or disable the flows.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
