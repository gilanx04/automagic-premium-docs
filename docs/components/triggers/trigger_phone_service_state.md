---
title: "Trigger - Phone Service State"
source: https://automagic4android.com/trigger_phone_service_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Phone Service State

The trigger **Phone Service State** is executed when the device detects the specified state.

Warning: Some devices don't send the current service state to applications when the screen is turned off. You can periodically use the action **Turn Screen On** to mitigate this problem.

Examples:

- Play a warning sound when no service is available.

### Settings

#### SIM

The SIM card.

#### Phone Service State

**In Service**
Execute the flow when the telephony is back to regular operation.

**Out of Service**
Execute the flow when telephony becomes unavailable.

**Emergency Only**
Execute the flow when only emergency numbers can be called.

**Power Off**
Execute the flow when the radio is explicitly powered off.

#### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. Consumes more battery when a shorter time interval is chosen.

#### Turn screen on

Whether the display should be turned on briefly or not. This option increases battery consumption and should only be enabled when the values are not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_service_state` — the previous service state (0=in service, 1=out of service, 2=emergency only, 3=power off)
- `service_state` — the current state of the service (0=in service, 1=out of service, 2=emergency only, 3=power off)
- `roaming` — boolean indicating the roaming status

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
