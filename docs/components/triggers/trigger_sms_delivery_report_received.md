---
title: "Trigger - Automagic SMS Delivery Report Received"
source: https://automagic4android.com/trigger_sms_delivery_report_received_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Automagic SMS Delivery Report Received

The trigger **Automagic SMS Delivery Report Received** is executed when an asynchronous delivery report was received.

Note: Multiple delivery reports can be received per SMS, for example a status 48 (delivery pending) and later status 0 (OK) when the SMS was delivered.

Examples:

- Send an SMS one more time when the delivery report indicates an error.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `sms_receiver` — the original receiver of the SMS
- `sms_text` — the original text of the SMS
- `sms_delivery_report_status` — the status code (0-31=OK, 32-63=delivery pending, >=64=error)

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
