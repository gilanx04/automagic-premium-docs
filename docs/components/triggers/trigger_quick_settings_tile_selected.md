---
title: "Trigger - Quick Settings Tile Selected"
source: https://automagic4android.com/trigger_quick_settings_tile_selected_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Quick Settings Tile Selected

The trigger **Quick Settings Tile Selected** configures the selected quick settings tile and is executed when the tile is selected/clicked.

Tip: Action **Update Quick Settings Tile** can be used to change the icon, label or state of the tile.

Examples:

- Create a QS tile to send an SMS with the current location.

### Settings

#### Tile

The tile to use.

#### Icon

The icon to use for the tile. [Variables are supported (replaced when trigger is activated).](../actions/action_script.md#string-inline-expressions)

#### Label

The label of the tile. [Variables are supported (replaced when trigger is activated).](../actions/action_script.md#string-inline-expressions)

#### Collapse panel

Whether or not the quick settings area should be closed when the tile is selected/clicked.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
