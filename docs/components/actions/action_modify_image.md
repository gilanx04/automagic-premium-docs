---
title: "Action - Modify Image"
source: https://automagic4android.com/action_modify_image_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Modify Image

The action **Modify Image** can be used to modify an image that was previously loaded with an action **Init Variable Image File**.

Examples:

- Load an image, shrink the size and send the smaller file by mail.

### Settings

#### Variable

The name of the variable holding the pixel data of the image. [Variables are supported.](action_script.md#string-inline-expressions)

#### Operation

The type of modification to apply to the image:

- *Scale*: change the size of the image either respecting the aspect ratio or by distorting the image
- *Rotate*: rotates the image by 90° or 180°
- *Mirror*: mirrors the image horizontally or vertically
- *Crop & Scale*: extracts the largest possible area from the center of the image by respecting the aspect ratio of the original image and scales to the desired size
- *Crop to Selection*: crops the image to the defined area

#### Width (Scale)

The new width of the image. The width is adjusted proportionally, when only the new height is specified. [Variables are supported.](action_script.md#string-inline-expressions)

#### Height (Scale)

The new height of the image. The height is adjusted proportionally, when only the new width is specified. [Variables are supported.](action_script.md#string-inline-expressions)

#### Rotate

How the image should be rotated.

#### Mirror

If the image should be mirrored horizontally or vertically.

#### Width (Crop & Scale)

The new width of the image. [Variables are supported.](action_script.md#string-inline-expressions)

#### Height (Crop & Scale)

The new height of the image. [Variables are supported.](action_script.md#string-inline-expressions)

#### X, Y (Crop to Selection)

The X and Y position of the selection. [Variables are supported.](action_script.md#string-inline-expressions)

#### Width, Height (Crop to Selection)

The width and height of the selection. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `image_data` — the local variable of the image
- `image_width` — the width of the image after the modification
- `image_height` — the height of the image after the modification

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
