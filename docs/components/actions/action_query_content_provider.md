---
title: "Action - Query Content Provider"
source: https://automagic4android.com/action_query_content_provider_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Query Content Provider

The action **Query Content Provider** allows to load data from a content provider of another app. A content provider presents data to Automagic as one or more tables that are similar to the tables found in a relational database.

Warning: This function allows to access data that's not officially made available by Android which might not be available on all device models and Android Version.

### Settings

#### Content URI

The URI of the content provider data. [Variables are supported.](action_script.md#string-inline-expressions)

#### Projection

The list of tables to return. [Variables are supported.](action_script.md#string-inline-expressions)

#### Selection

A filter declaring which rows to return, formatted like an SQL WHERE clause (excluding the WHERE itself). The selection can include ?-characters that will be replaced by the values provided in the *Selection Arguments* from the content provider. [Variables are supported.](action_script.md#string-inline-expressions)

#### Selection Arguments

The values to use in the selection for each provided ?-character. [Variables are supported.](action_script.md#string-inline-expressions)

#### Sort Order

How to order the rows, formatted as an SQL ORDER BY clause (excluding the ORDER BY itself). [Variables are supported.](action_script.md#string-inline-expressions)

#### Result Type

Defines how Automagic should provide the data to the flow:

- `Table`: Provides a list of rows each containing a list of values to the flow.
- `Table (transposed)`: Same as table but transposed. Provides a list for each column containing all values of the column.
- `List`: Converts the returned table to a flat list.
- `Single value`: Provides only the first value of the returned data to the flow.
- `Text`: Converts the returned table to a CSV-text.

#### Include header row

Whether or not the returned result should include a row with the column titles.

#### Variable

The name of the variable to store the result in. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `result` — the resulting data as defined in *Resultat-Typ*

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
