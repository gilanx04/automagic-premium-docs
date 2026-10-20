---
title: "Action - Init Variables Media Session (Experimental)"
source: https://automagic4android.com/action_init_variables_media_session_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Init Variables Media Session (Experimental)

The action **Init Variables Media Session (Experimental)** fills the information of the media session of the specified media player into variables.

Examples:

- Check if Google Play Music is playing a track.

### Settings

#### Package Names

The name of the media player to check. Glob patterns (\*, ?) are supported. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `playback_state` — current state (0=none, 1=stopped, 2=paused, 3=playing, 4=fast forwarding, 5=rewinding, 6=buffering, 7=error, 8=connecting, 9=skip to previous, 10=skip to next, 11=skip to item in queue)
- `playback_position` — current position in ms
- `title` — the title
- `subtitle` — the subtitle
- `description` — the description
- `icon` — the current image
- `icon_uri` — the URI to load the image
- `media_duration` — duration of the track in ms

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
