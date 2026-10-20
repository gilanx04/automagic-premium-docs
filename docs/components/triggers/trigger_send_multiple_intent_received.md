---
title: "Trigger - Send/Share Multiple Intent Received"
source: https://automagic4android.com/trigger_send_multiple_intent_received_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Send/Share Multiple Intent Received

The trigger **Send/Share Multiple Intent Received** is executed when the send/share menu is used in an app and multiple items are shared with Automagic.

Examples:

- Select multiple files in a file manager and share the files with Automagic.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `data_string` — the URI of the data this intent is targeting or null
- `mimetype` — the MIME type of the data being sent
- `texts` — the list of text items when available
- `stream_uris` — the list of URIs when available
- `html_texts` — optional texts as HTML when available
- `email` — the list of mail receivers when available
- `cc` — the list of mail addresses to CC
- `bcc` — the list of mail addresses to BCC
- `subject` — the subject when available

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
