---
title: "Trigger - Periodic Location Update"
source: https://automagic4android.com/trigger_periodic_location_update_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - Periodic Location Update

The trigger **Periodic Location Update** is executed in periodic intervals and delivers a location to the executed flow.
The accuracy of the location heavily depends on the selected location provider.

Tip: The higher the time interval between updates the less battery will be used. A frequency of about 4 minutes is recommended.

Examples:

- Record the location every 5 minutes to a file.
- Send an SMS with your location every hour to someone.

### Settings

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

#### Frequency

The desired time between location updates. The actual time between location updates depends on the location provider when **Enforce Exact Frequency** is not checked.
A location provider (for example GPS) can ignore the specified frequency and deliver updates every few seconds.

#### Enforce Exact Frequency

Ensures that the location is provided in the intervals specified by **Frequency** even when the location provider delivers the location updates more often or less often.

#### Minimum Accuracy (in meters)

Only newer locations with at least the specified accuracy are passed to the flow.
This can be useful to filter out locations calculated using the cell tower when also more exact locations using WiFi are available.

#### Limit time range

Whether the trigger should be active all the time or only within a defined time range.

#### Weekdays

The day on which the trigger should be active.

#### From - To

The start of the time range and the end of the time range. A To-time smaller than the From-time will move the To-time to the next day to simplify checks for time ranges crossing midnight.

#### Allow in device idle/doze (Android 6+)

Defines whether this trigger is allowed to wake the device from idle/doze mode. (see [Device Idle/Doze Mode](../../reference/device-idle-mode.md))

#### Like alarm clock (Android 5+)

Defines whether this trigger should be handled like an alarm clock which is usually displayed in the status bar.
This option ensures that Android invokes the trigger exactly at the specified time and prevents the system from delaying the event.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `location` — the reported location
- `location_accuracy` — the accuracy of the location
- `location_altitude` — the altitude of the location when available
- `location_bearing` — the direction of travel in degrees East of true North when available
- `location_speed` — the speed of travel in meters per second when available

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
