---
title: "Action - Execute Root Command"
source: https://automagic4android.com/action_execute_root_command_en.html
archived: 2022-12-02
archive_url: https://web.archive.org/web/20221202231448/https://automagic4android.com/action_execute_root_command_en.html
category: action
---

# Action - Execute Root Command

The action **Execute Root Command** executes a shell command as root by passing the command to `su` and stores the output in variables.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Examples:

- `reboot` to reboot the device
- `reboot -p` to shutdown

String variables are replaced before the command is passed to the interpreter.
You can use this for example to create a filename based on the current date: `ps > file-{triggertime,datetime,yyyyMMdd}.txt`.

Special characters in the command have to be escaped using backslash or placed in quotes as appropriate:
`cat 'Test File1.txt' > 'Test File2.txt'`
`cat Test\ File1.txt > Test\ File2.txt`

### Settings

#### Command

Enter the shell command to execute in this field. The command is passed to `su` to be interpreted.
The available commands vary from device to device. [Variables are supported.](action_script.md#string-inline-expressions)

#### User

The user to use for executing the command. Defaults to root when not specified. [Variables are supported.](action_script.md#string-inline-expressions)

#### SE Context

The SE context to use to execute the command. This setting is often required when using Android 5+ or any other device that set SELinux to enforcing. Requires *su* that allows to switch SE context (like SuperSU v1.97+). [Variables are supported.](action_script.md#string-inline-expressions)

#### Working Directory

The path the command is executed in. [Variables are supported.](action_script.md#string-inline-expressions)

#### Timeout

The timeout for the command.

#### Variable to store the standard output

The output written by the command to the standard output is stored in the variable defined in this field.

#### Variable to store the error output

The output written by the command to the error output is stored in the variable defined in this field.

#### Variable to store the exit code

The exit code of the command is stored in the variable defined in this field.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `stdout` — the standard output of the command
- `stderr` — the standard error output of the command
- `exit_code` — the exit code of the command

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
