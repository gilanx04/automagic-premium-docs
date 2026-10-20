---
title: "Action - Store Audio Volumes"
source: https://automagic4android.com/action_store_audio_stream_volume_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Store Audio Volumes

The action **Store Audio Volumes** stores the currently set audio volumes in global variables to restore using action **Restore Audio Volumes**.

Examples:

- Store the audio volumes when a meeting begins, set all volumes to zero and restore the previously volumes when the meeting ends.

### Settings

#### Alarm

Whether or not to store the alarm volume and the name of the variable to store the volume in.

#### DTMF

Whether or not to store the DTMF volume and the name of the variable to store the volume in.

#### Music

Whether or not to store the music volume and the name of the variable to store the volume in.

#### Notification

Whether or not to store the notification volume and the name of the variable to store the volume in.

#### Ring

Whether or not to store the ringtone volume and the name of the variable to store the volume in.

#### System

Whether or not to store the system volume and the name of the variable to store the volume in.

#### Voice Call

Whether or not to store the voice call volume and the name of the variable to store the volume in.

#### Ringer Mode

Whether or not to store the ringer mode and the name of the variable to store the value in.

#### Interruptions Mode

Whether or not to store the interruptions mode and the name of the variable to store the value in.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- names of the variables defined in the text fields — the volumes, ringer mode and interruptions mode as numbers

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
