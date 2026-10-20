---
title: "Device Idle / Doze Mode"
source: https://automagic4android.com/automagic/1.38/onlinehelp/en/device_idle_mode.html
archived: 2019-05-17
archive_url: https://web.archive.org/web/20190517133634/https://automagic4android.com/automagic/1.38/onlinehelp/en/device_idle_mode.html
category: reference
---

# Device Idle / Doze Mode

## What it is

Device Idle/Doze Mode is a battery saving method introduced by Android 6.
When a device is not plugged to a power source and is not moved for about one hour, the device enters the device idle/doze mode. In this mode alarms registered by apps are not executed anymore in general. Thus the CPU of the device has not to be activated that often anymore which should lead to a reduction in battery use.

An app can instruct Android to execute a few important alarms in this mode anyway but certain restrictions apply:

- Android will execute at most one such alarm per 15 minutes when the device *is* in idle/doze mode
- Android will execute at most one such alarm each minute when the device *is not* in idle/doze mode

Most time-based triggers like **Periodic Timer** and **Calendar Event** have an option called **Allow in device idle/doze** to define whether the trigger should ask Android to execute the trigger in device idle/doze mode.

When an app does not obey the restrictions but registers two alarms for almost the same time, Android delays the second alarm until one minute respectively 15 minutes have elapsed, depending on whether idle/doze mode is in effect or not.

This definition has the disadvantage that many flow combinations can not be implemented in a reliable way anymore since you might not know in advance if two alarms will violate the one-minute/15-minute restriction.

## Example

You might have a flow that plays a ringtone every morning at 6:00 and you have a second flow to play an alarm when a meeting starts (let's assume it starts at 6:05).
Android will not execute the two flows in device idle/doze mode when option **Allow in device idle/doze** is not active but will delay both triggers until the device is woken from device idle/doze mode.
With option **Allow in device idle/doze** enabled for both triggers, Android will play the sound at 6:00 and will execute the second flow at 6:05 when idle/doze mode is not in effect. The second flow will be delayed to run at 6:15 when doze mode happens to be in effect.

## Best practices

- Enable flags to execute triggers in device idle/doze mode only when the flow is really important like a calendar event notification, an alarm in the morning etc.
- Don't enable flags to execute triggers in device idle/doze mode when the trigger is executed frequently since it could delay more important flows.
- When an important flow is executed like an alarm in the morning, wake the device (see workarounds).

## Workarounds

- Wake device from idle/doze immediately when it falls into device idle/doze mode:

- trigger **Device Idle/Doze Mode: On**
- action **Turn Screen On** (or action **Exit Device Idle/Doze Mode** on a rooted device)

- Wake device from device idle/doze periodically so that the device executes normally for about an hour:

- trigger **Periodic Timer: every 1h or less frequently** (ensure to check **Allow in device idle/doze**)
- action **Turn Screen On** (or action **Exit Device Idle/Doze Mode** on a rooted device)

- Wake device from idle/doze when an important flow with **Allow in device idle/doze** is executed:

- trigger **Time: every day at 6:00** (ensure to check **Allow in device idle/doze**)
- action **Turn Screen On** (or action **Exit Device Idle/Doze Mode** on a rooted device)
- ...normal Actions of the flow...

---

[← Indeks referensi](README.md) · [Peta dokumentasi](../README.md)
