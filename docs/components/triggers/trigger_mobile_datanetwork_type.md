---
title: "Trigger - Mobile Datanetwork Type"
source: https://automagic4android.com/trigger_mobile_datanetwork_type_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Mobile Datanetwork Type

The trigger **Mobile Datanetwork Type** is executed when the network type switches to one selected in the list.

Examples:

- Play an alert sound when the network switches to GPRS.

### Settings

#### Network Type

The network types to execute the trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `previous_mobile_network_type` — the type of the network before
- `mobile_network_type` — the type of the network (0=Unknown, 1=GPRS, 2=EDGE, 3=UMTS, 4=CDMA, 5=CDMA - EvDo rev. 0, 6=CDMA - EvDo rev. A, 7=CDMA - 1xRTT, 8=HSDPA, 9=HSUPA, 10=HSPA, 11=iDEN, 12=CDMA - EvDo rev. B, 13=LTE, 14=CDMA - eHRPD, 15=HSPA+)

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
