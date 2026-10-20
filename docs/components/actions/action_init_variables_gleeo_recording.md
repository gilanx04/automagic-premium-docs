---
title: "Action - Init Variables Gleeo Recording"
source: https://automagic4android.com/action_init_variables_gleeo_recording_en.html
archived: 2022-10-06
archive_url: https://web.archive.org/web/20221006125806/https://automagic4android.com/action_init_variables_gleeo_recording_en.html
category: action
---

# Action - Init Variables Gleeo Recording

The action **Init Variables Gleeo Recording** checks if a task is recording in **Gleeo Time Tracker** and stores the recording project and task in variables.

Examples:

- Store the recording task when someone calls and start recording the same task again when the call ends.
- Don't use a funny alert sound when you are working for a special project.

### Settings

#### Variable for Recording Boolean

The name of the variable to store the boolean whether **Gleeo Time Tracker** is currently recording.

#### Variable for Recording Domain Title

The name of the variable to store the domain **Gleeo Time Tracker** is currently recording.

#### Variable for Recording Project Name

The name of the variable to store the project **Gleeo Time Tracker** is currently recording.

#### Variable for Recording Task Name

The name of the variable to store the task **Gleeo Time Tracker** is currently recording.

#### Variable for Recording Start Time

The name of the variable to store the start time of the currently recording task.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `recording` — the recording boolean
- `recording_domain_name` — the domain name
- `recording_project_title` — the project name
- `recording_task_name` — the task name
- `recording_start` — the start time of the currently recording task

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
