---
title: "Action - Take Picture"
source: https://automagic4android.com/action_take_picture_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Take Picture

The action **Take Picture** takes a picture using the built-in camera app or directly in the background without showing a user interface/preview (Android 4+)

Examples:

- Take a picture once an hour and upload the image to Dropbox.

### Settings

#### Recording Mode

Whether to use the camera app or to take the picture in the background without user interface (Android 4+).

#### Target File

The target file to save the picture. [Variables are supported.](action_script.md#string-inline-expressions)

#### Camera

The camera to use to take the picture.

#### Picture Size

The resolution of the image.

#### Zoom

The zoom ratio.

#### Scene Mode

The scene mode.

#### Flash Mode

Whether to use the flash or not.

#### White Balance

The white balance setting to use.

#### Focus Mode

The focus mode to use.

#### Effect

The effect to apply to the image. Not all effects work with all cameras. Often the effect is ignored for the front-facing camera.

#### Await preview images

Whether or not Automagic should await that the camera produces valid preview images before it takes the picture. Can be unchecked to take pictures faster or to workaround issues when the camera does not produce any preview images and thus runs into a timeout.

#### Delay to fix black picture

Whether or not and how long Automagic should delay taking the picture after the camera has been initialized by Android. On some devices a delay of about 2 seconds can prevent the camera from producing black pictures.

#### Add to gallery

Whether or not the image should be made available in the gallery app. Otherwise the picture will become available when the system scans the device for media files the next time.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `picture_path` — the target path of the picture

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
