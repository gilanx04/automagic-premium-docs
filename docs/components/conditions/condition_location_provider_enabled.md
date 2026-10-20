---
title: "Condition - Location Provider Enabled"
source: https://automagic4android.com/condition_location_provider_enabled_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Location Provider Enabled

The condition **Location Provider Enabled** checks whether a particular location provider like GPS is enabled or not.

Examples:

- Report your location per SMS only when GPS is active.

### Settings

#### Location Provider

The location provider to check.

**Network**
This provider uses the location provided by the cell tower and Wi-Fi signals. Depending on environment this provider can deliver location of about 60 meters of accuracy. Locations found using the cell tower can be very inaccurate (up to several kilometers or miles).

**Passive**
This provider delivers the location from the currently active provider (Network or GPS) without activating one of the providers by itself. This might result in very infrequent location updates.

**GPS**
This provider delivers the location using the GPS receiver. This provider usually uses more battery than the network provider.

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
