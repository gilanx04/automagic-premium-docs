---
title: "Condition - Expression"
source: https://automagic4android.com/condition_expression_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Expression

The condition **Expression** checks whether the expression is true or not.

Example Expressions:

- `a==1`
- `b > =3`
- `c < b AND a > 3`
- `(a--)==0`
- `startsWith(a, "test")`
- `a > addDays(b, 4)`
- `isEmpty(files)`

Examples:

- Check if the accuracy of a location is good enough: `location_accuracy<300`
- Check if a counter reached zero: `counter==0`

[See action Script for a description of the scripting language.](../actions/action_script.md)

### Settings

#### Expression

The expression to evaluate.

Note: Variables can be used directly in an expression and don't need to be escaped using curly braces.

Example: use `location_accuracy` instead of `{location_accuracy}`.

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
