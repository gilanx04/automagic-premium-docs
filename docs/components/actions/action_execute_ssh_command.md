---
title: "Action - Execute SSH Command (Experimental)"
source: https://automagic4android.com/action_execute_ssh_command_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001213600/https://automagic4android.com/action_execute_ssh_command_en.html
category: action
---

# Action - Execute SSH Command (Experimental)

The action **Execute SSH Command** connects to an SSH server and executes a command.

Note: It can not be guaranteed that this action is compatible with all SSH servers.

Examples:

- Execute a command on a NAS every evening.
- Show the free memory of the server on a widget.

### Settings

#### Server/Port

The IP or name of the SSH server to connect to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Validate host key

Whether the host key should be checked or not. Skipping the host key check reduces the security of SSH.

#### Username

The username. [Variables are supported.](action_script.md#string-inline-expressions)

#### Authentication type

Whether to use password authentication or public key authentication. Keyboard interactive authentication is not supported.

#### Password

The password.

#### Private key file

The path to the private key file (OpenSSH format). You may need to convert the key to another format when the key does not work in Automagic. [Variables are supported.](action_script.md#string-inline-expressions)

#### Public key file

The path to the public key file (OpenSSH format). You may need to convert the key to another format when the key does not work in Automagic. [Variables are supported.](action_script.md#string-inline-expressions)

#### Passphrase

The passphrase of the key or empty when no passphrase is used.

#### Test connection/Update host key

Tries to establish a connection to the specified server using the given credentials. Variables are not replaced.

#### Command

The command to execute. [Variables are supported.](action_script.md#string-inline-expressions)

#### Feed input file

Whether to feed an input file to the executed command (like *cat file | ssh user@server command*)

#### Input file

The file to feed to the command. [Variables are supported.](action_script.md#string-inline-expressions)

#### Timeout

The overall timeout (connect and execute).

#### Store stdout in a variable or file

Whether to store the output of the command in a variable (max. 1MB, text). Binary output should always be stored in a file.

#### Variable to store the standard output

The output written by the command to the standard output is stored in the variable defined in this field.

#### File to store the standard output

The path to the file to store the output of the command. [Variables are supported.](action_script.md#string-inline-expressions)

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
