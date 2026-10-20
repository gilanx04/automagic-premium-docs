---
title: "Action - Init Variable Package Info"
source: https://automagic4android.com/action_init_variable_package_info_en.html
archived: 2022-10-07
archive_url: https://web.archive.org/web/20221007123138/https://automagic4android.com/action_init_variable_package_info_en.html
category: action
---

# Action - Init Variable Package Info

The action **Init Variable Package Info** loads information of the specified apps/packages and stores the information in a map.

Tip: Condition **Debug Dialog** can be used to display the keys and values stored in the map.

Examples:

- Load the list of permissions used by an app and check which permissions have been granted.

## Format

The map contains the package name as the key and a map with the queried information as value. Example shown as JSON:
```
        {
          "package1": {"version_name": xyz, "version_code": 123},
          "package2": {"version_name": xyz, "version_code": 123}
        }
```

Example JSON queried for one app:
```
        {
          "com.android.vending": {
            "version_name": "6.4.12.C-all [0] 2744941", // the version name
            "version_code": 80641200, // the version number
            "first_install_time": 1230796800000, // the time at which the app was first installed (millis since 1970)
            "last_update_time": 1461091018180, // the time at which the app was last updated (millis since 1970)
            "install_location": -1, // -1=auto?, 0=auto, 1=internal only, 2=prefer external
            "application_info": {
              "data_dir": "/data/user/0/com.android.vending", // full path to a directory assigned to the package for its persistent data
              "class_name": "com.google.android.finsky.FinskyApp", // class implementing the Application object
              "source_dir": "/data/app/com.android.vending-2/base.apk", // full path to the base APK for this application
              "label": "Google Play Store", // the label of the app (current locale)
              "uid": 10024, // the kernel user-ID that has been assigned to this application
              "icon_uri": "android.resource://com.android.vending/2130903045", // URI to load the icon of the app
              "target_sdk_version": 23, // the API level that the application targets
              "enabled": true // whether or not the Android system can instantiate components of the application
            },
            "requested_permissions": [
              {
                "permission": "android.permission.WRITE_EXTERNAL_STORAGE", // the name of the permission
                "requested_permission_flag": 3, // 1=requested, 3=requested & granted
                "label": "modify or delete the contents of your USB storage", // the label of the permission
                "description": "Allows the app to write to the USB storage.", // the description of the permission
                "protection_level": 1, // protection level as number
                "protection_level_text": "dangerous", // protection level expressed as text
                "group": "android.permission-group.STORAGE", // the group name of the permission
                "group_label": "Storage", // the permission group label
                "group_description": "access photos, media, and files on your device" // the permission group description
              }, ...
            ],
            "activity_info": [
              {
                "name": "com.android.vending.AssetBrowserActivity",
                "label": "Play Store",
                "icon_uri": "android.resource://com.android.vending/2130903045",
                "enabled": true, // whether the activity is enabled
                "exported": true // whether the activity can be used by other apps
                "permission": "com.google.android..." // permission required to access this activity (when defined)
              },
            ],
            "receiver_info": [
              {
                "name": "com.google.android.gcm.GCMBroadcastReceiver",
                "label": "Google Play Store",
                "enabled": true,
                "exported": true,
                "permission": "com.google.android.c2dm.permission.SEND"
              }, ...
            ],
            "provider_info": [
              {
                "name": "com.google.android.finsky.providers.RecentSuggestionsProvider",
                "label": "Google Play Store",
                "authority": "com.google.android.finsky.RecentSuggestionsProvider",
                "enabled": true,
                "exported": false
              }, ...
            ],
            "service_info": [
              {
                "name": "com.google.android.finsky.services.ReviewsService",
                "label": "Google Play Store",
                "enabled": true,
                "exported": true
              }, ...
            ]
          }, ...
        }
```

Please note that additional key value pairs might be added in future versions of Automagic.

### Settings

#### Type

Whether to query information about all installed packages or only a few selected packages.

#### Package Names

The list of packages to query. Glob patterns (\*, ?) are supported. [Variables are supported.](action_script.md#string-inline-expressions)

#### Include permission infos

If information about permissions requested by the app should be queried.

#### Include activity infos

If information about activities defined by the app should be queried.

#### Include receiver infos

If information about receivers defined by the app should be queried.

#### Include provider infos

If information about content providers defined by the app should be queried.

#### Include service infos

If information about services defined by the app should be queried.

#### Variable

The name of the variable to store the result in.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `package_info` — the map containing the queried information

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
