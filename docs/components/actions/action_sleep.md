---
title: "Action - Sleep"
source: https://automagic4android.com/action_sleep_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Sleep

The action **Sleep** pauses the flow execution for a certain amount of time.

Note: Please uncheck the option *Keep device awake* when the period is longer than one to two minutes and the functions of the flow does not require an active device CPU.

Examples:

- Sleep a second when a vibrate action is executing.
- Slow down a countdown flow.

### Settings

#### Duration

The amount of time to sleep. [Variables are supported.](action_script.md#string-inline-expressions)

#### Keep device awake

Ensure that the device does not go into deep sleep while the action is executed.
Unchecking this option will not prevent the device from falling into deep sleep mode. The device will be woken up when the specified period has elapsed.

#### Wakeup from idle/doze (Android 6+)

Defines if this action is allowed resume from idle/doze mode. (see [Device Idle/Doze Mode](../../reference/device-idle-mode.md))

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
