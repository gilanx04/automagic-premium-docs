---
title: "Condition - Phone Service State"
source: https://automagic4android.com/condition_phone_service_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Phone Service State

The condition **Phone Service State** checks whether the phone service is currently available, unavailable or only emergency calls can be placed.

Warning: Some devices don't send the current service state to applications when the screen is turned off.

### Settings

#### SIM

The SIM card.

#### Phone Service state

The accepted states.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `service_state` — the state of the service (0=in service, 1=out of service, 2=emergency only, 3=power off)
- `roaming` — boolean indicating the roaming status

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
