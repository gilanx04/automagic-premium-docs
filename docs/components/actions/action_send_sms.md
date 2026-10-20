---
title: "Action - Send SMS"
source: https://automagic4android.com/action_send_sms_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Send SMS

The action **Send SMS** sends an SMS to the specified phone number.

Examples:

- Send an SMS with your location as a response to an SMS containing the text **Where are you?**.
- Send an SMS to your partner when you are on your way home.

### Settings

#### SIM

The SIM card.

#### To

The number to send the SMS to. [Variables are supported.](action_script.md#string-inline-expressions)

Example:

- use `{sms_sender}` to fill in the phone number received in an **SMS Received** trigger.

#### Message

The message to send. [Variables are supported.](action_script.md#string-inline-expressions)

Example:

- use `{location,locationformat}` to fill in a nearby address of the location. The location can be determined using an action **Init Variable Location**.

#### Truncate

Whether to truncate the message text to fit within one SMS or to send the message using multiple SMS parts.

#### SMS Sending Limit

Defines how many SMS can be sent within the given amount of time. The action interrupts the flow with an error when the limit is exceeded.

#### Store sent SMS

Whether to store the sent SMS in the sent messages of the devices messaging app or not. This function is not officially supported by Android and might not work on all devices. Android 4.4+ automatically stores all sent SMS.

#### Delivery Report Options

Whether to request a delivery report and whether the report should be synchronous which blocks the action until the report is received or the timeout elapsed or to asynchronously deliver the report to trigger *Automagic SMS Deliver Report Received*.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `sms_delivery_report_status` — the status code (0-31=OK, 32-63=delivery pending, >64=error)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
