---
title: "Condition - Phone Cell GSM"
source: https://automagic4android.com/condition_phone_cell_gsm_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Phone Cell GSM

The condition **Phone Cell GSM** checks whether the phone is connected to one of the specified cells of interest.

Examples:

- Turn on WiFi when the phone cell at home is detected.

### Settings

#### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

#### Location Area Code (LAC) List

A comma separated list of location area codes. A location area is set of base stations and usually covers a large area. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Cell ID (CID) List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `lac` — the currently connected location area code (LAC), -1 if unknown
- `cid` — the currently connected cell ID (CID), -1 if unknown
- `psc` — the primary synchronization code (PSC), -1 if unknown
- `neighboring_cells` — the list of neighboring cells. Null or empty if not available
- `cells` — the list of all known cells by the system. Null or empty if not available

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
