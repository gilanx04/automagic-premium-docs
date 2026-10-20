---
title: "Action - Scan Barcode"
source: https://automagic4android.com/action_scan_barcode_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Scan Barcode

The action **Scan Barcode** opens an activity to scan a barcode using the camera of the device.

Tip: You can use an action **Map Values** to map known barcode values like a QR code on a laboratory door to a project/task.

Examples:

- Start recording the time in **Gleeo Time Tracker** based on a barcode on a laboratory door.
- Scan a barcode on a book and open the browser to search the book on Amazon.

### Settings

#### Timeout

The timeout duration to automatically cancel the barcode scan.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `operation` — the operation used to close the scan barcode activity.

  Can be one of:
  - `ok` when a bar code has been successfully scanned
  - `cancel` when the user pressed the back button or another button to leave the activity
  - `timeout` when the activity was closed by a timeout
- `barcode_text` — the value of the barcode as a text string
- `barcode_format` — the format of the barcode

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
