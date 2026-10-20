---
title: "Action - Take Screenshot (Experimental)"
source: https://automagic4android.com/action_take_screenshot_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Take Screenshot (Experimental)

The action **Take Screenshot (Experimental)** creates a screenshot of the currently displayed screen.

Tip: Action **Execute Root Command: screencap -p image.png** can be used on many rooted devices to take a screenshot on older versions of Android.

Note: Android delivers the screen content compressed to Automagic, the quality of the image is not always optimal. Some devices only allow to take screenshots with a low resolution.

Note: Views that are marked as secure by the displaying app can not be recorded.

Note: The display has to be turned on to take a screenshot.

Examples:

- Create a screenshot and send the image as an attachment as an EMail when a special SMS is received.

### Settings

#### Resolution

The resolution.

#### File

The path of the file to store [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `operation` — "ok" when successful, "cancel" when interrupted
- `output_path` — the target path of the screenshot

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
