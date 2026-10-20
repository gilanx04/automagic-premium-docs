---
title: "Action - Start Service"
source: https://automagic4android.com/action_start_service_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Start Service

The action **Start Service** starts a service using the specified intent. Please also see the [documentation of the Android Intent class](http://developer.android.com/reference/android/content/Intent.html).

Tip: Some services require special permissions to be launched. Check the log after testing the action when a service fails to start.

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

The specific service to launch. [Variables are supported.](action_script.md#string-inline-expressions)

#### Flag List

The flags to add to the intent.

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

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
