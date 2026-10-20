---
title: "Action - Input Dialog"
source: https://automagic4android.com/action_input_dialog_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Input Dialog

The action **Input Dialog** shows an input dialog with an input text field, password field, single- or multi-selection list.

Examples:

- Ask the user whether he wants to turn WiFi off or not.
- Ask for the password to use for an FTP upload.
- Ask whether airplane mode should be activated in the evening. Activate airplane mode when the user does not respond within 30 seconds.

### Settings

#### Input Dialog Type

The type of the input dialog to show.

Can be one of:

- `Multi-line text` for multiple lines of plain text input
- `Single-line text` for a single line of plain text input
- `Password` for a password input
- `PIN` for a pin input
- `Number` to type number characters
- `Phone number` to type characters used in phone numbers
- `Date` to show a date picker
- `Time` to show a time picker
- `Date & Time` to show a dialog with a date & time picker
- `Single Choice Menu` for a list of values like a menu without OK, Cancel buttons
- `Multi Choice` for a list of values the user can choose multiple values from

#### Title

The title of the input dialog. [Variables are supported.](action_script.md#string-inline-expressions)

#### Prompt (only applicable to `Text` and `Password`)

The question or input description to show in the input dialog. [Variables are supported.](action_script.md#string-inline-expressions)

#### List Values (only applicable to `Single Choice` and `Multi Choice`)

A comma separated list of values to show as values the user can choose from. [Variables are supported.](action_script.md#string-inline-expressions)

#### Default Value

The default value provided when the user does not change the input value. This value is also provided when the user cancels the dialog or hits the back key. [Variables are supported.](action_script.md#string-inline-expressions)
Whether the user has cancelled the dialog can be evaluated using the variable `operation` (see below).

The default value for date/time input types must be formatted as specified below:

- `Date`: Pattern `yyyy-MM-dd` for example `2014-01-25` or when using a variable `{variable,dateformat,yyyy-MM-dd}`
- `Time`: Pattern `HH:mm` (24-hour format) for example `14:20` or when using a variable `{variable,dateformat,HH:mm}`
- `Date & Time`: Pattern `yyyy-MM-dd HH:mm` (time in 24-hour format) for example `2014-01-25 14:20` or when using a variable `{variable,dateformat,yyyy-MM-dd HH:mm}`

Values not formatted according to the rules above are ignored.

#### Font size

The size of the font used to enter text values.

#### Activate Timeout

Whether an automatic timeout should provide a value to the flow when the user does not react within the specified time.

#### Duration

The amount of time to automatically close the dialog and to continue the flow.

#### Value on Timeout

The value to provide to the flow when a timeout occurred. [Variables are supported.](action_script.md#string-inline-expressions)

#### Options

- *Show when locked*: Show the input dialog even when the device is locked
- *Turn screen on*: Turn the screen on when the dialog is shown initially
- *Keep screen on*: Keep the screen on as long as the dialog is shown (power button still allows turn off the screen)
- *Enlarge dialog width*: Enlarge the width of the dialog to cover almost the entire screen
- *Keyboard hint to capitalize sentences*: Give a hint to the keyboard that sentences should be started with an uppercase letter

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `operation` — the operation used to close the dialog.

  Can be one of:
  - `ok` when the user pressed the OK button
  - `cancel` when the user pressed the cancel button or the back key
  - `timeout` when the dialog was closed by a timeout
- `value` —
  the selected value in the dialog or the list of values in case of `Multi Choice` or a date when the input dialog type was of type date/time.
  `value` for type *time* is the entered time of the current date.
- `index` — the index of the selected value of a `Single Choice` list or -1 when not definable
- `indices` — the indices of the selected values of a `Multi Choice` list or -1 for every not definable value

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
