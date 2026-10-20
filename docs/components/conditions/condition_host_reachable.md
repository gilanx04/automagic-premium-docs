---
title: "Condition - Host Reachable"
source: https://automagic4android.com/condition_host_reachable_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Host Reachable

The condition **Host Reachable** tests whether a host can be reached by either opening a TCP-connection using a socket or by executing a ping command.

Examples:

- Check once an hour if a server can be reached or not.

### Settings

#### Type

Type of the check:

- **Automatic**: Tries to connect to the host to port 7 to determine if the host is available. This method might use ping on some versions of Android.
- **Socket**: Tries to establish a TCP-connection to the specified host and port. The host is only considered to be reachable when the connection can be successfully established.
- **Ping**: Checks the reachability of the host using a `ping`-command (only one echo-request is sent). This option only works when the `ping`-command is available on the device.

#### Host

The host to check. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Port

The port to connect to (only for type=Socket). [Variables are supported.](../actions/action_script.md#string-inline-expressions)

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
