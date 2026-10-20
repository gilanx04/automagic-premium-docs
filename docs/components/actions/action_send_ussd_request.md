---
title: "Action - Send USSD Request"
source: https://automagic4android.com/action_send_ussd_request_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Send USSD Request

The action **Send USSD Request** sends a USSD request to the provider.

Warning: Some versions of Android don't properly handle USSD request failures so a dialog of the system might be shown when a USSD request fails which causes the action to timeout after 30 seconds.

Examples:

- Query the prepaid balance.

### Settings

#### SIM

The SIM card.

#### USSD Request

The request to send. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `ussd_failure_code` —
- `ussd_response` — the response text

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
