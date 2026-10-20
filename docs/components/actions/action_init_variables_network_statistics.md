---
title: "Action - Init Variables Network Statistics"
source: https://automagic4android.com/action_init_variables_network_statistics_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Init Variables Network Statistics

The action **Init Variables Network Statistics** queries the transferred amount of data of the specified network interfaces.
The network statistics are recorded by the operating system itself and is stored in blocks of two hours (device dependent). Queries that don't fall on such a two hour limit, will be interpolated (device dependent) so results might not be accurate especially for short time intervals.
The data of the network statistics is stored for each UID (user identification) of the executed process. Many apps/packages of the system are aggregated under UID 1000 and can not be differentiated further. The package selection shows the UID in brackets.
Data not available to the network statistics of the device can not be considered by this action (e.g. when a device is factory reset).

Examples:

- Periodically check the amount of data transferred by a specific app and show a warning when 100 MB are exceeded.

### Settings

#### Network interface

Whether to return mobile and/or WiFi statistics data.

#### Date range

The date range to query.

#### Cycle start day

The day of month when the bill cycle starts. [Variables are supported.](action_script.md#string-inline-expressions)

#### From

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the start time of the event.

#### To

A script whose last statement must evaluate to a date (milliseconds since 1970) to use as the end time of the event.

#### Type

Whether to query information about all installed packages or only a few selected packages (based on UID).

#### Package Names for UIDs

The list of packages to query to determine the UIDs. Glob patterns (\*, ?) are supported. [Variables are supported.](action_script.md#string-inline-expressions)

#### State

Whether to return foreground and/or background data.

#### Variable for transmitted bytes

The name of the variable to store the transmitted bytes.

#### Variable for received bytes

The name of the variable to store the received bytes.

#### Variable for total bytes

The name of the variable to store the total transferred bytes.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `transmitted_bytes` — the transmitted data in bytes
- `received_bytes` — the received data in bytes
- `total_bytes` — the total transferred data in bytes

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
