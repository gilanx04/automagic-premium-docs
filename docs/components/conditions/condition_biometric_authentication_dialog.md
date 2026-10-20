---
title: "Condition - Biometric Authentication Dialog"
source: https://automagic4android.com/condition_biometric_authentication_dialog_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Biometric Authentication Dialog

The condition **Biometric Authentication Dialog** shows the authentication dialog of the system and validates a biometric attribute like a fingerprint.

The dialog is temporarily not shown by the system when the fingerprint scanning failed a few times.

Examples:

- Show an authentication dialog for security reasons before deleting a file.

### Settings

#### Title

The titel to show (mandatory). [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Subtitle

The subtitle to show (optional). [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Description

The description to show (optional). [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Cancel button label

The label of the cancel button (mandatory). [Variables are supported.](../actions/action_script.md#string-inline-expressions)

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
  - `success` when the user successfully authenticated
  - `failure` when the user failed to authenticate
  - `timeout` when the dialog was closed by a timeout
  - `cancel` when the user pressed the back button or back key
- `error_code` — Error code when the dialog was closed by an error
- `error_message` — Error description as text in case the dialog was closed by an error

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
