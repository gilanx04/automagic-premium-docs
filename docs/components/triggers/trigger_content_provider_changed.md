---
title: "Trigger - Content Provider Changed"
source: https://automagic4android.com/trigger_content_provider_changed_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Content Provider Changed

The trigger **Content Provider Changed** is executed whenever the content provider is changed for the specified URI. Note that not all content providers support this feature.

Examples:

- Get notified whenever the MMS database changes so you can check if there's a new message.

### Settings

#### Content URI

The URI to get changes for (including ancestors).

#### Notify for descendants

Whether changes in descendant URIs should also be detected.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `content_uri` — the actual URI for the change

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
