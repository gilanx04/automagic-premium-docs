---
title: "Action - Init Variables Phone Info"
source: https://automagic4android.com/action_init_variables_phone_info_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Init Variables Phone Info

The action **Init Variables Phone Info** initializes the desired variables (not all values are available on all devices).

Examples:

- Check the network operator once an hour.

### Settings

#### SIM

The SIM card.

#### Variable Device ID (e.g. IMEI/MEID/ESN)

The name of the variable.

#### Variable Software Version (e.g. IMEI/SV)

The name of the variable.

#### Variable Line 1 Number (e.g. MSISDN)

The name of the variable.

#### Variable Network Country ISO

The name of the variable.

#### Variable Network Operator (e.g. MCC+MNC)

The name of the variable.

#### Variable Network Operator Name

The name of the variable.

#### Variable Phone Type

The name of the variable.

#### Variable SIM State

The name of the variable.

#### Variable SIM Country ISO

The name of the variable.

#### Variable SIM Operator

The name of the variable.

#### Variable SIM Operator Name

The name of the variable.

#### Variable SIM Serial Number

The name of the variable.

#### Variable Subscriber ID (e.g. IMSI)

The name of the variable.

#### Variable Voice Mail Alpha Tag

The name of the variable.

#### Variable Voice Mail Number

The name of the variable.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `device_id` — the device ID (e.g. IMEI/MEID/ESN), null when unavailable
- `device_software_version` — the software version (e.g. IMEI/SV), null when unavailable
- `line1_number` — the phone number string for line 1 (e.g. MSISDN), null when unavailable
- `network_country_iso` — the ISO country code (only when registered to a network, unreliable on CDMA)
- `network_operator` — numeric network operator name MCC+MNC (only when registered to a network, unreliable on CDMA)
- `network_operator_name` — network operator name (only when registered to a network, unreliable on CDMA)
- `phone_type` — type of the phone (0=no, 1=GSM, 2=CDMA, 3=SIP)
- `sim_state` — State of the SIM (0=unknown, 1=absent, 2=PIN required, 3=PUK required, 4=network locked, 5=ready)
- `sim_country_iso` — SIM ISO country code
- `sim_operator` — SIM MCC+MNC (only available when SIM in state ready)
- `sim_operator_name` — service provider name SPN (only available when SIM in state ready)
- `sim_serial_number` — serial number of the SIM, null when unavailable
- `subscriber_id` — the subscriber ID (e.g. IMSI), null when unavailable
- `voice_mail_alpha_tag` — the alphabetic identifier associated with the voice mail number
- `voice_mail_number` — the voice mail number, null when unavailable

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
