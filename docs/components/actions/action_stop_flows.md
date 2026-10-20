---
title: "Action - Stop Flows"
source: https://automagic4android.com/action_stop_flows_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Stop Flows

The action **Stop Flows** stops one or multiple flows specified in the field **Flow pattern list** as soon as possible. Use an action **Set Flow State** to disable flows.

Examples:

- Stop a wake-up flow when the device is shaken.

### Settings

#### Flow pattern list

A comma separated list of flow names to stop. Glob patterns `*` and `?` can be used to match similar named flows.

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*battery save*`

#### Exclude flow pattern list

A comma separated list of flow names to **not** stop, even when the field **Flow pattern list** includes the flow.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
