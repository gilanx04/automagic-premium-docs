---
title: "Action - Sound"
source: https://automagic4android.com/action_sound_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Sound

The action **Sound** plays the selected sound.

Examples:

- Beep every 5 minutes when **Gleeo Time Tracker** is recording.
- Play an additional alert when an SMS is received.

### Settings

#### Sound Type

The type of sound to select.

Possible settings:

- **Built-in sound**: to select a built-in notification, alarm or ringtone
- **File**: to select an arbitrary audio file to play

#### Sound

The name of the selected ringtone, notification or alarm sound.

#### File

The path or the URL to the audio file to play. [Variables are supported.](action_script.md#string-inline-expressions)

#### Audio Stream Type

The stream to use to play the sound.

#### Start Position

The start position in milliseconds to use to start the playback. [Variables are supported.](action_script.md#string-inline-expressions)

#### Show status bar notification to stop sound

Shows a status bar notification when the sound is playing that stops the sound when selected.

#### Wait for sound to finish

Makes the action wait for the sound to finish before continuing with the next element in the flow.

#### Request audio focus

Defines whether or not and how Automagic should request audio focus. This causes other apps like music players to pause playback or to temporarily lower the volume.

Possible settings:

- **Transient**: Automagic requests temporary audio focus, other apps usually pause playback temporarily (depends on app)
- **Transient may duck**: Automagic requests temporary audio focus, other apps either temporarily pause playback or temporarily lower the volume (depends on app)
- **Normal**: Automagic requests the normal audio focus, other apps usually pause/stop playback (depends on app)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
