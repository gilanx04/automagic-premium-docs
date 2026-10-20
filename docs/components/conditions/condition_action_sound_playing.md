---
title: "Condition - Action Sound Playing"
source: https://automagic4android.com/condition_action_sound_playing_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Action Sound Playing

The condition **Action Sound Playing** checks if an action Sound is currently playing a sound.

Examples:

- Refresh a stop-button in a widget depending whether a sound is currently playing or not.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `sound_position` — the playback position of the sound in milliseconds (first sound if multiple playing), null when no sound is playing
- `sound_duration` — the total duration of the sound in milliseconds (first sound if multiple playing), null when the media framework of Android can not determine the duration (live stream etc.)

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
