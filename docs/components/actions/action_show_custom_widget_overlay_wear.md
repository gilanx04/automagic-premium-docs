---
title: "Action - Show Custom Widget Overlay (Android Wear)"
source: https://automagic4android.com/action_show_custom_widget_overlay_wear_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Show Custom Widget Overlay (Android Wear)

The action **Show Custom Widget Overlay (Android Wear)** displays a custom Widget (defined within Automagic) on an arbitrary position on the display.

Warning: This function is not officially supported by Android and might not work on all devices.

Examples:

- Show the battery percentage as a semi-transparent rectangle over the statusbar.
- Prevent accidental touches by displaying an overlay that covers the entire screen.
- Shade the screen to a darker level than the built-in screen brightness control allows by displaying a semi transparent overlay covering the entire screen.

### Settings

#### Android Wear device

The target device. [Variables are supported.](action_script.md#string-inline-expressions)

#### Overlay name

The name/identification of the overlay. The same name can be used to hide the overlay using action **Hide Custom Widget Overlay.**
The same identification can be used in multiple actions to display the same overlay in different configurations depending on situation (e.g.different settings when in landscape or portrait).

#### Widget

The name of the widget to display. [Variables are supported.](action_script.md#string-inline-expressions)

#### Width/Height

The size of the overlay. [Variables are supported.](action_script.md#string-inline-expressions)

#### Gravity

The position to align the overlay on the screen.

#### X/Y-Offset

The offset of the overlay relative to the gravity. [Variables are supported.](action_script.md#string-inline-expressions)

#### Draggable

Whether the overlay can be moved on the screen using Drag&Drop.

#### Opacity

The transparency respectively opacity of the widget.

#### Clickable

Whether the overlay should react to clicks/touches. Warning: A clickable overlay blocks the touches of underlying elements!

#### Stretch widget

Whether the widget should be stretched to fill the entire area of the overlay.

#### Attempt to show on top

Whether Automagic should attempt to show the widget on top of everything else (over statusbar and lock screen).
This option might not work on all devices, especially on newer versions of Android (Android 8+).
This option can prevent certain apps like video players to temporarily override the screen brightness.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
