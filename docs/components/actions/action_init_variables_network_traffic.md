---
title: "Action - Init Variables Network Traffic"
source: https://automagic4android.com/action_init_variables_network_traffic_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Init Variables Network Traffic

The action **Init Variables Network Traffic** initializes variables with the transmitted and received bytes since device boot of the system or a specific user ID that runs a given app.

Note: Some devices do not collect user/app specific values. This is also a known problem of Android 4.3.

Examples:

- Store the number of transferred data for each day in a log file.

### Settings

#### Traffic

Whether the overall transferred data of the system should be stored or the transferred data transmitted by a particular app (respectively user ID).

#### Variable for total transmitted bytes

The name of the variable to store the sent bytes since device boot.

#### Variable for total received bytes

The name of the variable to store the received bytes since device boot.

#### Variable for mobile transmitted bytes

The name of the variable to store the sent bytes since device boot on the mobile interfaces.

#### Variable for mobile received bytes

The name of the variable to store the received bytes since device boot on the mobile interfaces.

#### Package Name

The name of the package to check (respectively the user that runs the app). [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable for transmitted bytes

The name of the variable to store the sent bytes of the user ID running the specified app since device boot.

#### Variable for received bytes

The name of the variable to store the received bytes of the user ID running the specified app since device boot.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `total_transmitted_bytes` — number of sent bytes or -1 when the device does not support this statistic
- `total_received_bytes` — number of received bytes or -1 when the device does not support this statistic
- `mobile_transmitted_bytes` — number of sent bytes over the mobile interfaces or -1 when the device does not support this statistic
- `mobile_received_bytes` — number of received bytes over the mobile interfaces or -1 when the device does not support this statistic
- `uid_transmitted_bytes` — number of sent bytes of the user ID or -1 when the device does not support this statistic
- `uid_received_bytes` — number of received bytes of the user ID or -1 when the device does not support this statistic

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
