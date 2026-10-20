---
title: "Trigger - View Web URL Intent Received"
source: https://automagic4android.com/trigger_view_web_url_intent_received_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - View Web URL Intent Received

The trigger **View Web URL Intent Received** is executed when an app wants to show a URL in a browser.

Examples:

- Receive a URL request and read the text on a weather site aloud, forwarding all other URL to the browser to be displayed as usual.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `data_string` — the received URL (http:// or https://)
- `categories` — the list of categories
- `scheme` — the scheme of the received intent
- `type` — the explicitly set MIME type of the received intent

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
