---
title: "Action - Save Variable in Image File"
source: https://automagic4android.com/action_save_variable_image_file_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Save Variable in Image File

The action **Save Variable in Image File** saves the pixel data that was previously loaded with an action **Init Variable Image File** into a file.

Examples:

- Load an image, shrink the size and send the smaller file by mail.

### Settings

#### Variable

The name of the variable holding the pixel data of the image. [Variables are supported.](action_script.md#string-inline-expressions)

#### File

The path of the file to store the image in. The type is determined by the file extension. (.jpg, .webp and .png are supported). [Variables are supported.](action_script.md#string-inline-expressions)

#### Image quality

How much the file should be compressed (0=small file/bad image quality, 100=big file/good image quality). The image quality is ignored for PNG-files. [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
