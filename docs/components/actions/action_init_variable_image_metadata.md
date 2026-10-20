---
title: "Action - Init Variable Image Metadata"
source: https://automagic4android.com/action_init_variable_image_metadata_en.html
archived: 2024-02-22
archive_url: https://web.archive.org/web/20240222113951/https://automagic4android.com/action_init_variable_image_metadata_en.html
category: action
---

# Action - Init Variable Image Metadata

The action **Init Variable Image Metadata** extracts the metadata (e.g. Exif tags) from an image and stores the values in a map (key=label/name of the tag, value=description or raw value of the tag).

Example to read the GPS location in an action **Script**:
`location = getMapValue(image_metadata, "gps_location");`

Tip: Condition **Debug Dialog** can be used to display the keys and values stored in the map.

Examples:

- Extract the GPS location and the thumbnail from a JPEG image.

### Settings

#### File

The path to the image file. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable

The name of the variable to store the map with the values in. [Variables are supported.](action_script.md#string-inline-expressions)

#### Parse dates

Defines if date strings should be converted to proper date/time values or if the string should be stored as a string in the map.

#### Include metadata directory name

Whether to include the name of the metadata directory in the key of each read tag.

#### Get raw values

Defines if the metadata values should be converted to a human readable form or if the values should be loaded as is.

#### Extract thumbnail

Defines if an available thumbnail should be extracted from the metadata and stored in variable `thumbnail_image`.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `image_metadata` — the map containing the extracted tag names/labels and the extracted values for each tag
- `thumbnail_image` — the thumbnail image extracted from the image metadata

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
