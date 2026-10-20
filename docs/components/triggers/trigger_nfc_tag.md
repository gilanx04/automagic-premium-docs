---
title: "Trigger - NFC Tag"
source: https://automagic4android.com/trigger_nfc_tag_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - NFC Tag

The trigger **NFC Tag** executes the flow when an NFC tag is detected.
You can either write a special ID to the NFC tag that will be used to identify the tag and execute the flow (this is the recommended option to use when you have a writable NFC tag) or you can also read the ID of an existing NFC tag. This is especially useful for read-only NFC tags like the ones often found in credit cards or read-only NFC tags (Live Tags, Smart Tags etc.) of some device manufacturers. Please also check the `Tip` in the settings section of this page.

Note: Not all NFC tags are supported.

Examples:

- Turn on the airplane mode when an NFC tag in the bedroom is scanned.

### Settings

#### Tag Type

Whether an NFC tag is written using a specific ID defined in Automagic (recommended) or an existing NFC tag should be used (does not work with all tags, some devices show an app selection list when other apps are installed that also handle NFC tags).

#### Tag IDs

A comma separated list of tag IDs. Glob patterns can be used to match multiple tag IDs.

#### Write ID to NFC tag

Opens a screen to write the specified IDs to an NFC tag. The NFC tag must be writable and must be able to contain NDEF formatted data.
Multiple IDs can be written to the tag but the tag IDs must contain only regular characters, underscore and numbers.

Option **Write alternate tag information** on the writer screen allows to define whether or not different type of information should be written to the NFC tag.
Some devices show a warning dialog when a regular Automagic NFC tag is scanned since the tag contains a Web-URL.
Writing an alternate tag uses a different URL that avoids this warning message.

Android 4+: Option **Include Android Application Record** on the writer screen allows to define whether or not an additional AAR (Android Application Record) should be written to the tag.
An AAR uses slightly more space on the NFC tag but ensures that the tag is preferably handled by Automagic and not by another app.

#### Read ID from NFC Tag

Opens a screen to read the ID of an existing NFC tag. Glob patterns can be used to match multiple tag IDs.

Tip: Some devices contain apps that can handle generic NFC tags and are shown in a selection list when an NFC tag is scanned. Uninstall or deactivate unused apps when the selection dialog bugs you. You can deactivate apps in the system settings on an Android 4+ device (System settings->Apps->All, Select the app->Deactivate).
For example, you can disable the app **Tags** on a Galaxy Nexus to prevent the selection list from showing.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `nfc_tag_ids` — the scanned tag ID or a comma separated list when the tag contained multiple IDs

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
