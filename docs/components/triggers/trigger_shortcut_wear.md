---
title: "Trigger - Shortcut (Android Wear)"
source: https://automagic4android.com/trigger_shortcut_wear_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Shortcut (Android Wear)

The trigger **Shortcut (Android Wear)** is executed when a shortcut in the list of Shortcut is selected (see Start -> Shortcut).

Examples:

- Turn WiFi on by pressing the shortcut.
- Launch a settings application screen by pressing the shortcut.
- Start recording in Gleeo Time Tracker by pressing the shortcut.

### Settings

#### Title

The title/name of the shortcut to create. The title is used to identify the Shortcut-trigger in Automagic, which means that a shortcut can execute multiple triggers when two Shortcut-triggers use the same title.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `node_id` — the ID of the Wear node

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
