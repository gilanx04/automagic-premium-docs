---
title: "Action - Start Recording Audio"
source: https://automagic4android.com/action_start_recording_audio_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Start Recording Audio

The action **Start Recording Audio** starts recording the specified audio source to the defined file. Only one audio file can be captured at a time.
The recording can be stopped manually using the shown statusbar notification or by executing the action **Stop Recording Audio**.

Warning: Some audio sources are not supported on most devices due to technical or legal reasons.

Examples:

- Start recording the audio of an incoming call.
- Record the audio at night between 1am and 2am.
- Record the audio for 10 minutes when an SMS arrives and send the resulting audio file to your mail account.

### Settings

#### Audio Source

The audio source to record.

Warning: The voice audio sources are not supported on most devices due to technical or legal reasons.

#### Audio Encoder

The audio encoding to use to compress the recorded audio.

#### Maximum Duration

The maximum duration to use when recording audio.

#### File

The path of the file to store the recorded audio in. A file ending of `m4a` or `mp4` is recommended. [Variables are supported.](action_script.md#string-inline-expressions)

Example:

- `/mnt/sdcard/audio_{triggertime,dateformat,yyyy_MM_dd}.m4a` becomes `/mnt/sdcard/audio_2011_02_13.m4a`

#### Show status bar notification to stop recording

Shows a status bar notification when audio is recording to stop.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
