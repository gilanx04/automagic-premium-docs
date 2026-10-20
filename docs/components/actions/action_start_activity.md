---
title: "Action - Start Activity"
source: https://automagic4android.com/action_start_activity_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Start Activity

The action **Start Activity** starts an activity using the specified intent. Please also see the [documentation of the Android Intent class](http://developer.android.com/reference/android/content/Intent.html).

Tip: Some activities require special permissions to be launched. Check the log after testing the action when an activity fails to start.

Examples:

- Start a specific action exposed by another application.
- Start a Skype call:
  - Action: **android.intent.action.VIEW**
  - Data URI: **skype:echo123**
- Dial a number (without calling):
  - Action: **android.intent.action.DIAL**
  - Data URI: **tel:99**
- Starting a mail app with a predefined subject:
  - Action: **android.intent.action.SEND**
  - Data MIME Type: **text/plain**
  - Extras: **putString("android.intent.extra.SUBJECT", "test")**

### Settings

#### Action

The action to use in the intent. [Variables are supported.](action_script.md#string-inline-expressions)

#### Category List

The list of categories as a comma separated list to add to the intent. [Variables are supported.](action_script.md#string-inline-expressions)

#### Data URI

The data URI to set on the intent. [Variables are supported.](action_script.md#string-inline-expressions)

#### Mime Type

The mime type to set on the intent. [Variables are supported.](action_script.md#string-inline-expressions)

#### Package Name

The specific package to launch. [Variables are supported.](action_script.md#string-inline-expressions)

#### Class Name

The specific activity to launch. [Variables are supported.](action_script.md#string-inline-expressions)

#### Launch bounds (Android 7+)

Whether the activity should be started at the defined position and size. This feature only has an effect on devices supporting freeform mode.
[Variables are supported.](action_script.md#string-inline-expressions)

#### Flag List

The flags to add to the intent. Note that the flag `Intent.FLAG_ACTIVITY_NEW_TASK` is always added to the intent.

#### Extras

A script used to add an unlimited number of extras to the intent.

Additionally to the regular built in functions of Automagic also the following functions are available to add the extras to the intent:

- `putString(key, value)`
- `putBoolean(key, value)`
- `putFloat(key, value)`
- `putDouble(key, value)`
- `putByte(key, value)`
- `putShort(key, value)`
- `putChar(key, value)`
- `putInt(key, value)`
- `putLong(key, value)`
- `putUri(key, value)`
- `putBooleanArray(key, value)`
- `putByteArray(key, value)`
- `putIntArray(key, value)`
- `putIntegerArrayList(key, value)`
- `putLongArray(key, value)`
- `putFloatArray(key, value)`
- `putDoubleArray(key, value)`
- `putShortArray(key, value)`
- `putCharArray(key, value)`
- `putStringArray(key, value)`
- `putStringArrayList(key, value)`
- `putUriArray(key, value)`
- `putUriArrayList(key, value)`

Example:
```
putString("key1", "Hello");
putBoolean("key2", true);
putDouble("key3", 1.23);
putInt("key4", 42);
putInt("key5", a+4*b);
```

[See action Script for a description of the scripting language.](action_script.md)

#### Wait for result

Whether Automagic should wait for the activity to return a result (only works when supported by the activity).

#### Access Result Extras

Script to access the extras in the returned intent.
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

[See action Script for a description of the scripting language.](action_script.md)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `result_code` — the returned result code
- `operation` — string "ok", when result\_code was -1, "cancel" otherwise
- `action` — the action of the received intent
- `data_string` — the data of the received intent as a string
- `categories` — the list of categories
- `scheme` — the scheme of the received intent
- `type` — the explicitly set MIME type of the received intent

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
