---
title: "Trigger - General Broadcast"
source: https://automagic4android.com/trigger_general_broadcast_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - General Broadcast

The trigger **General Broadcast** dynamically registers a broadcast receiver at runtime with the specified intent filter.
 Please also see the [Android Developer Documentation](http://developer.android.com/guide/components/intents-filters.html).

Examples:

- Receive the current WiFi signal strength (only when the display is turned on):
  Action: `android.net.wifi.RSSI_CHANGED`
  Access Intent Extras: `value=getInt("newRssi", 0);`

### Settings

#### Action

The action to use in the intent filter.

#### Category List

The list of categories to use in the intent filter.

#### Data Scheme List

The list of data schemes to use in the intent filter. (like `http`, `content` etc.).

#### Data Authority List

The list of data authorities to use in the intent filter (`host:port`).

#### Data Path Literal List

The list of data paths to use in the intent filter (the specified pattern has to match the entire path)

#### Data Path Prefix List

The list of data paths to use in the intent filter (the specified pattern has to match the prefix of the path)

#### Data Path Glob List

The list of data paths to use in the intent filter (the specified glob pattern has to match the entire path)

#### Data Type List

The list of MIME types to use in the intent filter.

#### Access Intent Extras

Script to access the extras in the received intent.
Following functions are supported:

- `getString(String key)`
- `getChar(String key, String defaultValue)`
- `getBoolean(String key, Boolean defaultValue)`
- `getFloat(String key, Number defaultValue)`
- `getDouble(String key, Number defaultValue)`
- `getByte(String key, Number defaultValue)`
- `getShort(String key, Number defaultValue)`
- `getInt(String key, Number defaultValue)`
- `getLong(String key, Number defaultValue)`
- `getBundle(String key)`
- `getUri(String key)`
- `getBooleanArray(String key)`
- `getByteArray(String key)`
- `getShortArray(String key)`
- `getCharArray(String key)`
- `getIntArray(String key)`
- `getIntegerArrayList(String key)`
- `getLongArray(String key)`
- `getFloatArray(String key)`
- `getDoubleArray(String key)`
- `getStringArray(String key)`
- `getUriArray(String key)`
- `getUriArrayList(String key)`
- `getParcelableAsString(String key)`
- `getParcelableArrayAsString(String key)`
- `getParcelableArrayListAsString(String key)`
- `getParcelable(String key)`

Examples:
```
    value = getString("key1");
    value = getBoolean("key2", true);
    value = getDouble("key3", 1.23);
    value = getInt("key4", 42);
    value = getInt("key5", a+4*b);
```

Data of intents wrapped in a Bundle-extra can be accessed using function `getBundle(String name)`.
Values contained in a bundle can be accessed with the functions used to accessed regular extras but by additionally specifying the bundle.

Example:
```
    bundle = getBundle("key1");
    value = getString(bundle, "key2");
```

compact form:
```
    value = getString(getBundle("key1"), "key2");
```

Example to access the track info of PowerAMP:
```
    track_info = getBundle("track");

    artist = getString(track_info, "artist");
    album = getString(track_info, "album");
    title = getString(track_info, "title");
    path = getString(track_info, "path");
    duration = getInt(track_info, "dur", 0);
```

#### Initial Sticky Broadcast

Whether to ignore the initial broadcast sent for a sticky broadcast or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `action` — the action of the received intent
- `data_string` — the data of the received intent as a string
- `categories` — the list of categories
- `scheme` — the scheme of the received intent
- `type` — the explicitly set MIME type of the received intent

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
