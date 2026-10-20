---
title: "Trigger - Shortcut"
source: https://automagic4android.com/trigger_shortcut_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Shortcut

The trigger **Shortcut** is executed when a shortcut on the launcher is pressed.
You can create the shortcut and select an icon by pressing the **Install Shortcut** button.

Note: Starting with Android 8 the install shortcut button might not have any effect. In this case you can create the shortcut by saving the trigger then going to the launcher, long press a free area, select *Widgets* then *AM Shortcut* to create a new shortcut.

Examples:

- Turn WiFi on by pressing the shortcut.
- Launch a settings application screen by pressing the shortcut.
- Start recording in Gleeo Time Tracker by pressing the shortcut.

### Settings

#### Title

The title/name of the shortcut to create. The title is used to identify the Shortcut-trigger in Automagic, which means that a shortcut can execute multiple triggers when two Shortcut-triggers use the same title. The title is passed to the launcher at the time when the button **Install Shortcut** is pressed.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
