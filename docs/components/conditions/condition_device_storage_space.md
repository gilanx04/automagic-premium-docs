---
title: "Condition - Device Storage Space"
source: https://automagic4android.com/condition_device_storage_space_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Device Storage Space

The condition **Device Storage Space** checks the storage space on the filesystem containing the specified path.

Example:

- Check every morning if 100MB are still free on the SD card.

### Settings

#### Filesystem

The path of the filesystem to check. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Compare Free or Used Space

Whether to check the free or used space on the filesystem.

#### Size

The size to check.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `available_blocks` — the number of free blocks available to applications
- `free_blocks` — the number of free blocks inclusive reserved blocks not usable by applications
- `block_count` — the total number of blocks in the filesystem
- `block_size` — the size of the blocks in bytes
- `available_space` — the available space in bytes
- `used_space` — the used space in bytes

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
