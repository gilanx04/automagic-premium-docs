---
title: "Trigger - Phone Signal Strength"
source: https://automagic4android.com/trigger_phone_signal_strength_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Phone Signal Strength

The trigger **Phone Signal Strength** is executed when the signal strength falls under or raises over the specified value.

Warning: Some devices don't send the current signal strength to applications when the screen is turned off.

Examples:

- Play an alert when the signal strength becomes bad.

### Settings

#### SIM

The SIM card.

#### Signal Strength Condition

Defines the condition that must be met to execute the flow:

**becomes lower than**
Executes the flow when the last reported value was above the defined level and the current value is below the defined level

**becomes higher than**
Executes the flow when the last reported value was below the defined level and the current value is above the defined level

**becomes equal to**
Executes the flow when the last reported value was different than the defined level and the current value equals the defined level

**lower than**
Executes the flow whenever the reported value by the system is below the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last value has been the same.

**higher than**
Executes the flow whenever the reported value by the system is above the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last value has been the same.

**exactly**
Executes the flow whenever the reported value by the system is exactly on the defined level. Depending on device this might cause the flow to be executed every few seconds. The flow is executed even when the last value has been the same.

#### Signal Strength

Defines the signal strength to use.

#### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. Consumes more battery when a shorter time interval is chosen.

#### Turn screen on

Whether the display should be turned on briefly or not. This option increases battery consumption and should only be enabled when the values are not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `is_gsm` — true when GSM
- `signal_strength_level` — the signal strength in a value from 0 to 4 like the bars on a standard Android device
- `signal_strength_asu` — the signal strength in ASU (0-31)
- `gsm_signal_strength` — the GSM signal strength (0-31, 99 for unknown, -1 for unavailable)
- `gsm_bit_error_rate` — the GSM bit error rate (0-7, 99 for unknown, -1 for unavailable)
- `cdma_dbm` — the CDMA RSSI value in dBm (-1 for unavailable)
- `cdma_ecio` — the CDMA Ec/Io value in dB\*10 (-1 for unavailable)
- `evdo_dbm` — the EVDO RSSI value in dBm (-1 for unavailable)
- `evdo_ecio` — the EVDO Ec/Io value in dB\*10 (-1 for unavailable)
- `evdo_snr` — the EVDO signal to noise ratio (0-8, -1 for unavailable)
- `lte_dbm` — the LTE RSRP value in dBm (-1 for unavailable)

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
