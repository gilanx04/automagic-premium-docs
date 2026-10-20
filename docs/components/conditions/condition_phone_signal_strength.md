---
title: "Condition - Phone Signal Strength"
source: https://automagic4android.com/condition_phone_signal_strength_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Phone Signal Strength

The condition **Phone Signal Strength** checks whether the signal strength of the mobile network is above or below a certain level.

Warning: Some devices don't send the current signal strength to applications when the screen is turned off. You can use the options to periodically turn the screen on or wake the device.

Examples:

- Beep every five minutes when the network strength is very weak.

### Settings

#### SIM

The SIM card.

#### Signal Strength Condition

Defines the condition that must be met to execute the flow:

**lower than**
true when the reported signal strength by the system is below the defined level

**higher than**
true when the reported signal strength by the system is above the defined level

**exactly**
true when the reported signal strength by the system is exactly on the defined level

#### Signal Strength

Defines the signal strength to use.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

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

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
