---
title: "Trigger - Location"
source: https://automagic4android.com/trigger_location_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Location

The trigger **Location** is executed when the location is entering the defined region or exiting the defined region.
The accuracy of the location depends heavily on the available location provider.

Tip: Enabling GPS in the phone settings can yield much better location accuracy but might use more battery. Locations with WiFi access points might work accurate enough and GPS can be disabled in the global phone settings to reduce battery strain.

Examples:

- Start recording in Gleeo Time Tracker when you are in the office, stop recording when you leave.
- Switch the ringer to vibrate when you are at your office.
- Turn off the ringer in the church. (Do it manually when it is important!)
- Send an SMS when you are home.

Note: The location is usually checked every 4 minutes when the device is not actively used and the classic method is used. This can result in the GPS icon on the statusbar being visible every 4 minutes. Entering/exiting a location can be missed when you are moving fast through a location with a small radius and the 4 minute check misses the location.
Locations can be reported more often when the device is active or another application also uses the location features (for example when using Google Maps).

### Settings

#### Method

The method used to detect the geofence.
*Modern* uses the new geofence API provided by Google and should be tuned to use only a minimum amount of battery power.
The algorithms to detect the locations are not known and can vary depending on device model. Please experiment with both methods to see what works best for you.

#### Location

The location used by this trigger.

#### Location Name

The name to use for this location. This name is used in the trigger name and to select an existing location on the map.

#### Radius

The radius around the location in meters.

#### Entering/Exiting

Whether to execute the flow when the location within the defined radius is entered or exited.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `location` — the configured location
- `location_name` — the name of the location
- `entering` — whether the location has been entered or not

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
