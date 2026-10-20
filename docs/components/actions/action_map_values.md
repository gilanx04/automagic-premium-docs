---
title: "Action - Map Values"
source: https://automagic4android.com/action_map_values_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Map Values

The action **Map Values** takes an input value (the key) and maps it to an output value.

Examples:

- Scan the barcode on the laboratory door and map the value to a project/task to start the time tracker.

### Settings

#### Input Value

The input value to map to another value. [Variables are supported.](action_script.md#string-inline-expressions)

Examples:

- `{barcode_text}` to map a barcode
- `{incoming_number}` to map the number of an incoming call

#### Mapping Definition

The definition used to specify how the values should be mapped to the target values. [Variables are supported.](action_script.md#string-inline-expressions)

Mapping example:
`key1=>value1`
`key2=>value2`

The part before the assignment operator (`=>`) is used to specify the key values to match. A comma separated list can be used to specify multiple keys for one target value. Glob pattern characters `*` and `?` can also be used to match multiple values.
The part after the assignment operator (`=>`) defines the target value to use as the map value.
The mapping rules are evaluated line by line from top to bottom. The first matching rule is applied.

Multi key mapping example:
`key1=>value1`
`key2,key3,key4=>value2`

Glob pattern mapping example:
`key1=>value1`
`key?=>value2`
`key*=>value3`

In the above example, the value `key1` would be mapped to `value1` because it is the first line matching the input value.
The values `key2` to `key9` would be matched by the second rule.
The value `key123` would be matched by the third rule.

When no rule matches the output value is set to `null`.

If you want to map a few known bar codes to meaningful task names but also want to use the plain barcode when no mapping rule matches, you can use the following approach (the input value would be set to `{barcode_text}` in this example):

Mapping definition:
`123321123=>Meeting`
`989878945=>Office`
`*=>{barcode_text}`

The third rule matches all unknown bar code values and maps the value to the original value. You can also use a condition **Expression** to detect not mappable values.

The last twenty not mappable values detected while executing the action will be remembered in a list and can be added by using the button **Add unmapped values...**

#### Output Variable

The name of the variable to store the result in (usually without curly braces except when you want to create dynamically named variables). [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `mapped_value` — the target value

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
