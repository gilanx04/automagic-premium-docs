---
title: "Trigger - Phone Cell GSM"
source: https://automagic4android.com/trigger_phone_cell_gsm_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Phone Cell GSM

The trigger **Phone Cell GSM** is executed when the device connects or disconnects from the defined cells. Changes within the defined list of cells don't invoke the trigger.

Warning: Some devices don't report the cell to Automagic when the screen is turned off.

Examples:

- Turn WiFi on, when the device connects to one of the cells at home.

### Settings

#### Method

Whether the classic, a modern or both methods should be used to find cells. It's highly device dependent which method works best.

#### Trigger when

Whether the trigger should execute the flow when connected/disconnected from an area defined by a list of cells or on every cell change (can be frequent).

#### Location Area Code (LAC) List

A comma separated list of location area codes. A location area is set of base stations and usually covers a large area. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Cell ID (CID) List

A comma separated list of cell IDs. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Cell ID (CID) List to Ignore

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
- `lac` — the currently connected cells location area code (LAC), -1 if unknown
- `cid` — the currently connected cells ID (CID), -1 if unknown
- `psc` — the currently connected cells primary synchronization code (PSC), -1 if unknown
- `last_lac` — the last connected cells location area code (LAC), -1 if unknown or the trigger was just activated
- `last_cid` — the last connected cells ID (CID), -1 if unknown or the trigger was just activated
- `last_psc` — the last connected cells primary synchronization code (PSC), -1 if unknown or the trigger was just activated
- `connected` — true when connected to the defined cells, false otherwise
- `disconnected` — true when disconnected from the defined cells, false otherwise

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
