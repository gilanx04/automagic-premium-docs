---
title: "Action - Compare Images"
source: https://automagic4android.com/action_compare_images_en.html
archived: 2022-12-03
archive_url: https://web.archive.org/web/20221203000906/https://automagic4android.com/action_compare_images_en.html
category: action
---

# Action - Compare Images

The action **Compare Images** compares two images pixel by pixel and provides an output image that shows the differences in the selected color and provides variables containing the total number of equal and different pixels.

Examples:

- Compare two screenshots to check if the screen contents differ.

### Settings

#### Image 1 Variable

The name of the variable containing the first image to compare.

#### Top/Left Inset Image 1

The top/left inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](action_script.md#string-inline-expressions)

#### Bottom/Right Inset Image 1

The bottom/right inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](action_script.md#string-inline-expressions)

#### Image 2 Variable

The name of the variable containing the second image to compare.

#### Top/Left Inset Image 2

The top/left inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](action_script.md#string-inline-expressions)

#### Bottom/Right Inset Image 2

The bottom/right inset to ignore in the comparison. The value can either be specified as a number of pixels (without suffix) or a percentage by appending the percent sign. [Variables are supported.](action_script.md#string-inline-expressions)

#### Tolerance

The tolerance that specifies how different the two compared pixels on the two images are allowed to be to still be considered equal.[Variables are supported.](action_script.md#string-inline-expressions)
Examples:

- 0=no tolerance, pixels have to be absolutely equal
- 0.1=a bit of tolerance, pixels can be a slightly different and still be considered equal

#### Output Color for Differences

The color to use on the resulting image to indicate the differences. Equal pixels are transparent on the resulting image.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `image_data` — the resulting image containing the different pixels in the specified color
- `equal_pixel_count` — the number of equal pixels
- `different_pixel_count` — the number of different pixels

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
