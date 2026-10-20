---
title: "Action - Execute Command"
source: https://automagic4android.com/action_execute_command_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071058/https://automagic4android.com/action_execute_command_en.html
category: action
---

# Action - Execute Command

The action **Execute Command** executes a shell command and stores the output in variables.

Examples:

- `ls -l` to list all files in the working directory
- `ps` to store the running processes in the defined variable
- `ps > file.txt` to store the running processes in a file
- `cat file1.txt > file2.txt` to copy a file
- `cat /proc/wakelocks` to show the wake locks preventing your device from sleeping

String variables are replaced before the command is passed to the interpreter.
You can use this for example to create a filename based on the current date: `ps > file-{triggertime,datetime,yyyyMMdd}.txt`.

Special characters in the command have to be escaped using backslash or placed in quotes as appropriate:
`cat 'Test File1.txt' > 'Test File2.txt'`
`cat Test\ File1.txt > Test\ File2.txt`

### Settings

#### Command

Enter the shell command to execute in this field. The command is passed to `/bin/sh` to be interpreted.
The available commands vary from device to device. [Variables are supported.](action_script.md#string-inline-expressions)

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
