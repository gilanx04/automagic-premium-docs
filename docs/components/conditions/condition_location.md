---
title: "Condition - Location"
source: https://automagic4android.com/condition_location_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Location

The condition **Location** checks whether a location is inside a specific area or not. The condition can also check if an area is entered or exited by comparing the location of the last execution and the current location.

The condition uses the location already made available to the flow from a location trigger or uses the last known location of the system.
The condition fails when no location is available in the flow and the device does not have a last known location ready. This usually happens when the flow is executed manually. Either use one of the location triggers to execute your flow or explicitly acquire the location using an action **Init Variable Location** before the condition is reached.

Examples:

- Enable WiFi when you enter your office.
- Stop recording in **Gleeo Time Tracker** when you leave your office.

### Settings

#### Location

The location used by this condition.

#### Location Name

The name to use for this location. This name is used in the condition name and to select an existing location on the map.

#### Radius

The radius around the location in meters.

#### Entering

True when the location was outside the defined location and is inside now.

#### Exiting

True when the location was inside the defined location and is outside now.

#### Ignore when previous state was not known

Ignore entering/exiting when the location has not been known before. This is usually the case when the flow is executed for the first time after starting **Automagic**.

#### Inside

True when the location is inside. This is also true when the location has been inside before and therefore is possibly true for every location provided by a trigger.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `location` — the reported location
- `location_name` — the name of the location
- `entering` — whether the location has been entered or not
- `exiting` — whether the location has been exited or not
- `inside` — whether the location is inside the defined area or not

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
