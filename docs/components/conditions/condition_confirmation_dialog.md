---
title: "Condition - Confirmation Dialog"
source: https://automagic4android.com/condition_confirmation_dialog_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Confirmation Dialog

The condition **Confirmation Dialog** shows a dialog with a question and continues flow execution depending on the button pressed.

Examples:

- Turn on bluetooth but ask for confirmation first.

### Settings

#### Title

The optional title of the dialog. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Question

The text of the question to ask. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### False Button / True Button

The text labels of the buttons that execute the true/false-branch of the condition. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Behavior on Back button

Whether to ignore the back button or to confirm the dialog with true or false.

#### Activate Timeout

Whether an automatic timeout should be used when the user does not react within the specified time.

#### Duration

The amount of time to automatically close the dialog and to continue the flow.

#### Value on Timeout

Whether the flow should be continued on the true- or false-branch.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `operation` — the operation used to close the dialog.

  Can be one of:
  - `yes` when the user pressed the Yes-button
  - `no` when the user pressed the No-button
  - `timeout` when the dialog was closed by a timeout
  - `cancel` when the user pressed the back key and the appropriate option is set

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
