---
title: "Action - Gleeo Create Entry"
source: https://automagic4android.com/action_gleeo_create_entry_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001203615/https://automagic4android.com/action_gleeo_create_entry_en.html
category: action
---

# Action - Gleeo Create Entry

The action **Gleeo Create Entry** creates an entry of the specified project and task in **Gleeo Time Tracker**.

Examples:

- Track the amount of time spent in the Twitter app and create an entry in Gleeo Time Tracker at the end of the day.

### Settings

#### Domain

The name of the domain to create an entry for. [Variables are supported.](action_script.md#string-inline-expressions)

#### Project

The name of the project to create an entry for. [Variables are supported.](action_script.md#string-inline-expressions)

#### Task

The task of the entry to create. The task will be created in **Gleeo Time Tracker** when it not already exists.
The task name can be defined dynamically using variables.

Examples:

- `Phone Support for {incoming_number}` becomes `Phone Support for 17001111111`
- `Visiting {trigger}` becomes `Visiting Customer X` (use different location triggers named `Customer X`, `Customer Y` etc.)

#### Details

The details of the entry. [Variables are supported.](action_script.md#string-inline-expressions)

#### Extra 1

Extra 1 of the entry. [Variables are supported.](action_script.md#string-inline-expressions)

#### Extra 2

Extra 2 of the entry. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable containing the start time

The name of the variable (without curly braces) containing the start time. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable containing the end time

The name of the variable (without curly braces) containing the start time. [Variables are supported.](action_script.md#string-inline-expressions)

#### Move to Background

Whether to move **Gleeo Time Tracker** to the background when the entry has been created.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
