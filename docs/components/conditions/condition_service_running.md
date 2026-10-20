---
title: "Condition - Service Running"
source: https://automagic4android.com/condition_service_running_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Service Running

The condition **Service Running** checks whether the specified service is currently running.

### Settings

#### Service Class

The class name of the service to check. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `package_name` — the package name of the service
- `service_name` — the display name of the service
- `pid` — the process this service is running in
- `uid` — the user id owning this service
- `active_since` — the time this service has been started (in milliseconds since the device was booted)
- `last_activity_time` — the time this service was last active (in milliseconds since boot not counting sleep phases)
- `restarting` — the time when this service will be started, 0 when the service is currently running
- `foreground` — true when the service is run as a foreground process

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
