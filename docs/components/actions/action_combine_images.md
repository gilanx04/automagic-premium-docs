---
title: "Action - Combine Images"
source: https://automagic4android.com/action_combine_images_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071052/https://automagic4android.com/action_combine_images_en.html
category: action
---

# Action - Combine Images

The action **Combine Images** allows to superimpose two images on top of each other. The images have to be loaded with action **Init Variable Image File**.

Note: The action has to create a copy of the image in memory so please ensure to scale down the images first when memory becomes an issue.

Examples:

- Superimpose a logo on an image as a watermark.

### Settings

#### Variable with first image (DST)

The variable containing the base image. The result is saved in this variable. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable with second image (SRC)

The variable containing the image to combine with the first one. [Variables are supported.](action_script.md#string-inline-expressions)

#### Mode

How to combine the two images.

#### Alignment of second image

The alignment of the second image on the first one.

#### X/Y-Offset

The offset of the second image relative to the gravity. [Variables are supported.](action_script.md#string-inline-expressions)

#### Opacity of second image

The opacity of the second image. [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
