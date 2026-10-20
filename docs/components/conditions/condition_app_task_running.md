---
title: "Condition - App Task Running"
source: https://automagic4android.com/condition_app_task_running_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - App Task Running

The condition **App Task Running** checks whether a task for one of the specified packages is currently running.

Warning: This function is not officially supported by Android 5+ and might not work on all devices.

### Settings

#### Method

How the app should be determined. Method **Usage statistics** can be delayed on some devices.

#### Package Name

The name of the app to check. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### check most recent app task only

if only the most recent app task should be checked (this is the active app on many Android versions)

Warning: This option must be activated on Android 5+.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `package_name` — the package name of the foreground app
- `index` — the index of this task. An index of zero denotes the most recent running task.
- `base_activity` — the component launched as the first activity in the task
- `top_activity` — the activity component at the top of the history stack of the task
- `id` — a unique identifier for this task
- `num_running` — the number of activities that are currently running (not stopped and persisted) in this task
- `description` — a description of the task's current state

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
