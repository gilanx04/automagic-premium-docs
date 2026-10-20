---
title: "Action - Control Audio Player"
source: https://automagic4android.com/action_control_audio_player_en.html
archived: 2024-12-08
archive_url: https://web.archive.org/web/20241208222719/https://automagic4android.com/action_control_audio_player_en.html
category: action
---

# Action - Control Audio Player

The action **Control Audio Player** can launch and control the default audio player of Android. Note that device and manufacturer specific audio players will probably not work.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Pause the audio player when the headphones are disconnected.

### Settings

#### Control Type

Defines the method used to control the media player:

- **Media Button**: Simulates the press of a media button
- **Broadcast**: Sends a broadcast to the audio service

#### Media Button

The button to press (not all apps handle all buttons):

- **Play**: Starts to play (Android >3)
- **Play/Pause**: Toggles between play and pause
- **Pause**: Pauses the audio player (Android >3)
- **Stop**: Stops the audio player
- **Previous**: Plays the previous track
- **Next**: Plays the next track
- **Fast forward**: Fast forward
- **Rewind**: Rewind
- **Eject**: Ejects the media (for example a CD tray) (Android >3)
- **Close**: Closes the media tray (for example a CD tray) (Android >3)
- **Record**: Starts to record (Android >3)
- **Track**: Switches the audio track (Android >4.4)

#### send to specified app

Whether to let the system choose the app to handle the media button or if the media button event should be sent to a specific app. This is mostly useful when multiple audio players are installed and the event is not handled by the desired player.

#### Package Name

The app to send the media button event to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Class Name

The component inside the app that should handle the media button. [Variables are supported.](action_script.md#string-inline-expressions)

#### Action

The action to execute:

- **Launch**: Launches the audio player
- **Play**: Starts to play
- **Play/Pause**: Toggles between play and pause
- **Pause**: Pauses the audio player
- **Stop**: Stops the audio player
- **Previous**: Plays the previous track
- **Next**: Plays the next track
- **Cycle Repeat**: Activates the next cycle mode
- **Toggle Shuffle**: Toggles the shuffle mode on/off

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
