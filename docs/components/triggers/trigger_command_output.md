---
title: "Trigger - Command Output"
source: https://automagic4android.com/trigger_command_output_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Command Output

The trigger **Command Output** is executed when a command prints a line containing a specific text.

### Settings

#### Command

The command to execute. The command is passed to `/bin/sh` to be interpreted or to `su` when *as root* is checked.

#### SE Context

The SE context to use to execute the command. This setting is often required when using Android 5+ or any other device that set SELinux to enforcing. Requires *su* that allows to switch SE context (like SuperSU v1.97+).

#### Working Directory

The path the command is executed in.

#### Output trigger condition

The text which needs to be contained in the output to trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `stdout` — the last 10 lines written to stdout
- `stderr` — the last 10 lines written to stderr
- `output` — the triggering line
- `output_type` — the string `stdout` when the triggering line was written to stdout, stderr otherwise

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
