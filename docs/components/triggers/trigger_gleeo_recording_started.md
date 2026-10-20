---
title: "Trigger - Gleeo Recording Started"
source: https://automagic4android.com/trigger_gleeo_recording_started_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Gleeo Recording Started

The trigger **Gleeo Recording Started** is executed when a task in **Gleeo Time Tracker** has been started.

### Settings

#### Domain Filter List

A comma separated list of the domains to accept.

#### Project Filter List

A comma separated list of the projects to accept.

#### Task Filter List

A comma separated list of the tasks to accept.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `domain_name` — contains the name of the domain
- `project_title` — contains the title of the project
- `task_name` — contains the name of the task
- `start` — contains the start date and time of the recording entry

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
