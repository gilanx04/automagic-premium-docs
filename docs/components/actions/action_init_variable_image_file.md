---
title: "Action - Init Variable Image File"
source: https://automagic4android.com/action_init_variable_image_file_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071056/https://automagic4android.com/action_init_variable_image_file_en.html
category: action
---

# Action - Init Variable Image File

The action **Init Variable Image File** loads the pixel data of an image into the specified local variable to modify the image with action **Modify Image** or to read color values of pixels with script function **getPixelColor**.

Warning: Loading large images uses a lot of internal memory which could cause Automagic to crash in the worst case. It's recommended to read only one image into memory and not to load very large images.

Examples:

- Load an image, shrink the size and send the smaller file by mail.

### Settings

#### File

The path or URL to the image file. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable

The name of the local variable to store the pixel data. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `image_data` — the local variable of the image
- `image_width` — the width of the image
- `image_height` — the height of the image

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
