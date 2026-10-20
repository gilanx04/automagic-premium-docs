---
title: "Action - Execute Flows"
source: https://automagic4android.com/action_execute_flows_en.html
archived: 2022-10-06
archive_url: https://web.archive.org/web/20221006124833/https://automagic4android.com/action_execute_flows_en.html
category: action
---

# Action - Execute Flows

The action **Execute Flows** executes one or multiple flows specified in the field **Flow pattern list**.

Tip: It's also possible to execute utility flows that don't have their own trigger. Simply don't add a trigger to such a flow but ensure that the flow is enabled.

The executed flow will inherit the execution context with all variables of the parent flow.
The variables usually supplied by the trigger of the target flow will not be available since the trigger of the target flow is bypassed when using this action.

Examples:

- Execute all flows with the words **battery save** in the name when the battery reaches a critical level.

### Settings

#### Flow pattern list

A comma separated list of flow names to execute. Glob patterns `*` and `?` can be used to match similar named flows.

Examples:

- `Test Flow`
- `Test Flow, SMS Flow`
- `*battery save*`

#### Exclude flow pattern list

A comma separated list of flow names to **not** execute even when the field **Flow pattern list** includes the flow.

#### Skip disabled flows without error

Whether disabled flows should be skipped without error or if the flow should be stopped with an error.

#### Wait for called flows to finish

Whether the action should wait until all called flows have been finished or not.

#### Return variables to the calling flow

Whether the local variables of the called flow should be returned to the calling flow.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `flow_count` — the number of flows to execute

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
