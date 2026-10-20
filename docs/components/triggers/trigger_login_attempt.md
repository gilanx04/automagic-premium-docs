---
title: "Trigger - Login Attempt"
source: https://automagic4android.com/trigger_login_attempt_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Login Attempt

The trigger **Login Attempt** is executed, whenever someone unsuccessfully tries to login to the device respectively tries to unlock the device.

Examples:

- Take a picture with the front camera when someone enters the wrong PIN code three times.

### Settings

#### Failed/Successful after failed

- **Failed:** executes the trigger when the login attempt fails
- **Successful after failed:** executes the trigger when the login attempt was successful after it failed one or multiple times before

#### When

- **On every failed attempt:** executes once for every failed attempt
- **On the Nth failed attempt:** executes the trigger exactly once when the number of failed login attempts reach the specified amount of times

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `failed_login_attempt` — the number of failed login attempts

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
