---
title: "Trigger - UI Event"
source: https://automagic4android.com/trigger_user_interface_event_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - UI Event

The trigger **UI Event** executes a flow when the system detects a change in the user interface, for example when a window is opened, a button is pressed, a list is scrolled, text has been entered etc.

Note: The system informs Automagic not about all events. Some events that occur very frequently can be skipped by the system.

Examples:

- Execute a flow, when the Install button in Google Play is pressed.

### Settings

#### Event Type

- *Window opened*: A new window, dialog or popup has been opened. The variable `text` often contains the title of the window.
- *Component clicked*: A button or label has been clicked. The variable `text` of image buttons is often empty.
- *Component long clicked*: A button or label has been long clicked. The variable `text` of image buttons is often empty.
- *Component selected*: An element has been selected, e.g. a row in a list or an element in a dropdown.
- *Component focused*: The input focus has been moved to another element.
- *Component scrolled*: A list has been scrolled.
- *Text changed*: The text in a text input fields has been changed.
- *Text selection changed*: The text selection or cursor position has been changed.
- *Announcement*: An app made an announcement like changing the page in a book.

#### Package Name

The list of apps to consider by this trigger. Glob patterns (\*, ?) are supported.

#### Text

The text that should be contained in the event.

#### Remove non-printable characters from text

Whether non-printable unicode characters should be removed from the text like left-to-right marks that might be used in components on the user interface.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `event_type` —
  the event represented by a number:
  - *Window opened*: `32`
  - *View clicked*: `1`
  - *View long clicked*: `2`
  - *View selected*: `4`
  - *View focused*: `8`
  - *Text changed*: `16`
  - *Text selection changed*: `8192`
  - *View scrolled*: `4096`
  - *Announcement*: `16384`
- `content_description` — the content description of the source
- `package_name` — the package name of originating app
- `source_class_name` — the class name of the source
- `source_bounds` — the position and size of the element (null when not determinable)
- `text` — the text of the source or the title of the opened window
- `label` — the label of the source
- `enabled` — whether the source is enabled
- `checked` — whether the source is checked
- `fullscreen` — whether the source is executed in fullscreen mode
- `password` — whether the source is a password field
- `scrollable` — whether the source can be scrolled
- `scroll_x` — the scroll offset of the source left edge in pixels
- `scroll_y` — the scroll offset of the source top edge in pixels
- `from_index` — from index of the element
- `to_index` — to index of the element
- `item_count` — number of elements in a list
- `current_item_index` — item position when the element is contained in a list
- `added_count` — number of added characters when a text is edited
- `removed_count` — number of removed characters when a text is edited
- `before_text` — text before it was changed
- `app_name` — the name of the originating app

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
