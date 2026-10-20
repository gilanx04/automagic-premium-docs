---
title: "Action - Init Variables Media Metadata"
source: https://automagic4android.com/action_init_variables_media_metadata_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Init Variables Media Metadata

The action **Init Variables Media Metadata** loads the metadata of a media file into local variables (see variables section below).

Examples:

- Load the title of an mp3 and show the title in a notification.

### Settings

#### File

The path or URL to the media file. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `media_cd_track_number` — the order of the audio data source on its original recording or null
- `media_album` — the album title or null
- `media_artist` — the artist or null
- `media_author` — the author or null
- `media_composer` — the composer or null
- `media_date` — the date when the data source was created or modified or null
- `media_genre` — the content type or genre or null
- `media_title` — the title or null
- `media_year` — the year when the data source was created or modified or null
- `media_duration` — the playback duration in milliseconds or null
- `media_num_tracks` — the number of tracks or null
- `media_writer` — the writer (such as lyricist) or null
- `media_mimetype` — the mime type or null
- `media_albumartist` — the performers/artist or null
- `media_disc_number` — the disc number or null
- `media_compilation` — the music album compilation or null
- `media_has_audio` — true if the media contains audio content
- `media_has_video` — true if the media contains video content
- `media_video_width` — the width of the video or null
- `media_video_height` — the height of the video or null
- `media_bitrate` — the bitrate of the media (in bits/sec) or null
- `media_location` — the location or null
- `media_video_rotation` — the video rotation angle in degrees or null
- `media_album_art` — the album art or null

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
