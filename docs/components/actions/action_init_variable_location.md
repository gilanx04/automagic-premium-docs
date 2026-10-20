---
title: "Action - Init Variable Location"
source: https://automagic4android.com/action_init_variable_location_en.html
archived: 2023-12-04
archive_url: https://web.archive.org/web/20231204163716/https://automagic4android.com/action_init_variable_location_en.html
category: action
---

# Action - Init Variable Location

The action **Init Variable Location** acquires one location from the defined provider and stores the location in the variable.

Note: Getting one location can take several seconds to complete. The passive provider might not return a location until another app is activating one of the location providers.

Examples:

- Send the location in response to an SMS containing the text **Where are you?** to the sender.
- Store the location coordinates in a file when the employer calls.
- Send the location and phone number by mail whenever you call someone.

### Settings

#### Variable

The name of the variable to store the location in.

#### New or Last Known Location

Defines if the action should acquire a new location or if the action should use the last known location. Loading the last known location uses almost is very fast but might return an outdated location or no location might be available when the device was freshly started.

#### Location Provider

The location provider to use.
**Network**
This provider uses the location provided by the cell tower and Wi-Fi signals. Depending on environment this provider can deliver location of about 60 meters of accuracy. Locations found using the cell tower can be very inaccurate (up to several kilometers or miles).

**Passive**
This provider delivers the location from the currently active provider (Network or GPS) without activating one of the providers by itself. This might result in very infrequent location updates.

**GPS**
This provider delivers the location using the GPS receiver. This provider usually uses more battery than the network provider.

**High Accuracy (Experimental)**
This provider delivers the finest available location using different sensors available on the device.

**Balanced Power/Accuracy (Experimental)**
This provider delivers the a location with an accuracy of about 100m and uses less battery than the high accuracy provider.

**Low Power (Experimental)**
This provider delivers the a location with an accuracy of about 10km.

**No Power (Experimental)**
This provider will only deliver locations when another app on the device has requested locations.

#### Minimum Accuracy (in meters)

Only newer locations with at least this accuracy are accepted.
This can be useful to filter out locations calculated using the cell tower when also more exact locations using WiFi are available.

#### Timeout

The maximum amount of time to wait for a location fix, otherwise terminate the flow with an error.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `location` — the reported location
- `location_accuracy` — the accuracy of the location
- `location_altitude` — the altitude of the location when available (not available on all devices)
- `location_bearing` — the direction of travel in degrees East of true North when available (not available on all devices)
- `location_speed` — the speed of travel in meters per second when available (not available on all devices)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
