---
title: "Action - Gleeo Start Recording"
source: https://automagic4android.com/action_gleeo_start_recording_en.html
archived: 2022-12-02
archive_url: https://web.archive.org/web/20221202235552/https://automagic4android.com/action_gleeo_start_recording_en.html
category: action
---

# Action - Gleeo Start Recording

The action **Gleeo Start Recording** starts recording the defined project and task in **Gleeo Time Tracker** when this task is not already recording.

Examples:

- Start tracking the time when you arrive at your office.
- Start tracking the time when your employer calls.
- Start tracking the time when you press a shortcut on the launcher.

### Settings

#### Domain

The name of the domain to start recording. [Variables are supported.](action_script.md#string-inline-expressions)

#### Project

The name of the project to start recording. [Variables are supported.](action_script.md#string-inline-expressions)

#### Task

The task to start recording. The task will be created in **Gleeo Time Tracker** when it not already exists.
[Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `Phone Support for {incoming_number}` becomes `Phone Support for 17001111111`
- `Visiting {trigger}` becomes `Visiting Customer X` (use different location triggers named `Customer X`, `Customer Y` etc.)

#### Details

The details of the entry. [Variables are supported.](action_script.md#string-inline-expressions)

#### Extra 1

Extra 1 of the entry. [Variables are supported.](action_script.md#string-inline-expressions)

#### Extra 2

Extra 2 of the entry. [Variables are supported.](action_script.md#string-inline-expressions)

#### Move to Background

Whether to move **Gleeo Time Tracker** to the background when the task has been started.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
