---
title: "Trigger - Phone Cell CDMA"
source: https://automagic4android.com/trigger_phone_cell_cdma_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Phone Cell CDMA

The trigger **Phone Cell CDMA** is executed when the device connects or disconnects from the defined cells. Changes within the defined list of cells don't invoke the trigger.

Warning: Some devices don't report the cell to Automagic when the screen is turned off.

Examples:

- Turn WiFi on, when the device connects to one of the cells at home.

### Settings

#### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

#### Trigger when

Whether the trigger should execute the flow when connected/disconnected from an area defined by a list of cells or on every cell change (can be frequent).

#### Cell List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Cell List to Ignore

A comma separated list of cell IDs to ignore. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Connected / Disconnected

Whether the trigger should be executed when the device connects or disconnects from the listed cells. Changes within the defined list of cells don't invoke the trigger.

#### Wake device

Whether the trigger should wake the CPU of the device every X minutes or not. This is necessary for some devices when the cell is not updated regularly. Consumes more battery when a shorter time interval is chosen.

#### Turn screen on

Whether the display should be turned on briefly or not. This is necessary for some devices when the cell is not updated otherwise. This option increases battery consumption and should only be enabled when the cell is not updated otherwise.

#### Force update

Whether the cell update should be forced. This option increases battery consumption and should only be enabled when the cell is not updated otherwise.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `cell_id` — the cell id, null if unknown
- `base_station_id` — the ID of the base station , -1 if unknown
- `network_id` — the ID of the network, -1 if unknown
- `system_id` — the ID of the system, -1 if unknown
- `base_station_latitude` — the latitude of the base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `base_station_longitude` — the longitude of the base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `last_cell_id` — the last cell id, null if unknown or the trigger was just activated
- `last_base_station_id` — the last ID of the base station , -1 if unknown or the trigger was just activated
- `last_network_id` — the last ID of the network, -1 if unknown or the trigger was just activated
- `last_system_id` — the last ID of the system, -1 if unknown or the trigger was just activated
- `last_base_station_latitude` — the latitude of the last base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `last_base_station_longitude` — the longitude of the last base station in quarter degree seconds, 2147483647 if unknown. Divide value by 14400 to get decimal degrees. Not all networks provide meaningful values.
- `connected` — true when connected to the defined cells, false otherwise
- `disconnected` — true when disconnected from the defined cells, false otherwise

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
