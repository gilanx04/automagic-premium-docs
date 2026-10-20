---
title: "Condition - Custom Widget Overlay Showing"
source: https://automagic4android.com/condition_custom_widget_overlay_showing_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Custom Widget Overlay Showing

The condition **Custom Widget Overlay Showing** checks if a particular custom widget is currently showing as an overlay.

Note: Android sometimes temporarily hides overlays for security reasons. This condition can not detect this circumstance and might assume that the widget is showing.

Examples:

- Execute some actions of a flow only when a particular overlay is showing.

### Settings

#### Overlay Name List

The names of the overlays to check. The condition evaluates to true when at least one of the overlays is showing. Glob patterns (\*, ?) are supported. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
