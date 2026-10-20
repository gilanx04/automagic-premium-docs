---
title: "Condition - Phone Cell CDMA"
source: https://automagic4android.com/condition_phone_cell_cdma_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Phone Cell CDMA

The condition **Phone Cell CDMA** checks whether the phone is connected to one of the specified cells of interest.

Examples:

- Turn on WiFi when the phone cell at home is detected.

### Settings

#### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

#### Cell List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

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
- `neighboring_cells` — the list of neighboring cells. Null or empty if not available
- `cells` — the list of all known cells by the system. Null or empty if not available

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
