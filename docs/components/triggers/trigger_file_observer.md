---
title: "Trigger - File Observer"
source: https://automagic4android.com/trigger_file_observer_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - File Observer

The trigger **File Observer** is executed when a path of interest on the filesystem is accessed or changed.

Examples:

- Create a copy of a file after it has been modified.
- Upload a new image to Dropbox when a new subfile is created in folder `/sdcard/DCIM/Camera/`.

### Settings

#### Paths to Observe

A comma separated list of files or directories to observe. [Variables are supported (replaced when trigger is activated).](../actions/action_script.md#string-inline-expressions)

#### Event Types

The type of events to observe.

- **File accessed**: Data was read from a file
- **Modify**: Data was written to a file
- **Metadata changed**: Metadata (permissions, owner, timestamp) was changed explicitly
- **Writable file closed**: Someone had a file or directory open for writing, and closed it
- **Unwritable file closed**: Someone had a file or directory open read-only, and closed it
- **File opened**: A file or directory was opened
- **File moved from**: A file or subdirectory was moved from the monitored directory
- **File moved to**: A file or subdirectory was moved to the monitored directory
- **Subfile created**: A new file or subdirectory was created under the monitored directory
- **Subfile deleted**: A file was deleted from the monitored directory
- **Delete Self**: The monitored file or directory was deleted; monitoring effectively stops
- **Self moved**: The monitored file or directory was moved; monitoring continues

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `registered_path` — the path of the observed file or directory
- `event` — the event represented as a number:
  - **File accessed**: 1 (0x00000001)
  - **Modify**: 2 (0x00000002)
  - **Metadata changed**: 4 (0x00000004)
  - **Writable file closed**: 8 (0x00000008)
  - **Unwritable file closed**: 16 (0x00000010)
  - **File opened**: 32 (0x00000020)
  - **File moved from**: 64 (0x00000040)
  - **File moved to**: 128 (0x00000080)
  - **Subfile created**: 256 (0x00000100)
  - **Subfile deleted**: 512 (0x00000200)
  - **Delete Self**: 1024 (0x00000400)
  - **Self moved**: 2048 (0x00000800)
- `path` — the path of the file or directory which triggered the event, relative to the main monitored file or directory

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
