---
title: "Action - Control UI"
source: https://automagic4android.com/action_control_user_interface_en.html
archived: 2023-12-21
archive_url: https://web.archive.org/web/20231221071056/https://automagic4android.com/action_control_user_interface_en.html
category: action
---

# Action - Control UI

The action **Control UI** uses the accessibility features of the device to control the user interface and allows to automatically press buttons, long-click elements, scroll lists and change the values of checkboxes and radio buttons.

Note: This action controls the user interface by simulating user input, therefore the screen has to be active, unlocked and the user interface must be showing on screen.
The accessibility service of Automagic needs to be enabled in the preferences for this action to work. At least Android 4.1 (Jelly Bean) is required.

Note: Turning on the accessibility service is not possible on some devices when a screen brightness or screen filter app displays an overlay over other controls. Please disable such apps temporarily when pressing the OK button in system settings is not possible.

Examples:

- Start the location settings page and enable/disable GPS.
- Start the device update check by pressing the "Check now" button.

### Settings

#### Script

Defines the actions to execute.
[See action Script for a description of the basic features of the scripting language.](action_script.md#string-inline-expressions)

Warning: The following example scripts are highly device specific! Please only use the scripts for reference and don't just copy/paste the scripts. It might click the wrong control elements on your device.

Clear all notifications:
```
notifications();//to expand the notifications
sleep(1000);//wait one second for animations to complete
clicked = click("Clear all notifications");//click the button
if(not clicked) //check whether the button has been successfully clicked
{
    back();//hide the notification when the clear button was not available
}
```

Toggle GPS on/off:
Use an action **Launch App: Settings/Location services** to directly start the GPS settings page
```
sleep(1000);//wait for settings page to show
click("GPS satellites");//toggle setting on/off
sleep(500);
back();//go back to the previous screen
```

Open the Apps drawer:
```
home();//ensure the main home screen is showing
sleep(1000);//wait one second for animations to complete
click("Apps");//open the apps drawer
```

## Supported Functions

- `Boolean sleep(Number milliseconds)`
  Waits for the specified amount of `milliseconds`.
- `Boolean sleep(String duration)`
  Waits for the specified amount of `milliseconds`.
- `Boolean back()`
  Presses the back key.
- `Boolean home()`
  Presses the home key.
- `Boolean notifications()`
  Expands the statusbar.
- `Boolean quickSettings()`
  Opens the quick settings of the status bar.
- `Boolean recents()`
  Opens the recent application list.
- `Boolean powerDialog()`
  Opens the power long-press dialog. (Android 5+)
- `Boolean toggleSplitScreen()`
  Toggles the split screen mode. (Android 7+)
- `Boolean lockScreen()`
  Locks the screen (Android 9+)
- `Boolean takeScreenshot()`
  Takes a screenshot (Android 9+)
- `Boolean click(String pattern)`
  Clicks on the element containing the given glob `pattern`.
- `Boolean click(Number x, Number y)`
  Clicks on the element at the specified location.
- `Boolean clickById(String id)`
  Clicks on the element with the given `id`. (Android 4.3+)
- `Boolean clickByIdAndIndex(String id, Number index)`
  Clicks on the n-th element with the given `id`. (Android 4.3+)
- `Boolean touchGesture(Number startMillis, Number endMillis, List coordinates, ...)`
  Simulates touch screen input by replaying the given coordinates within the specified amount of time. (Android 7+)
- `Boolean longclick(String pattern)`
  Longclicks on the element containing the given glob `pattern`.
- `Boolean longclick(Number x, Number y)`
  Longclicks on the element at the specified location.
- `Boolean longclickById(String id, Number index)`
  Longclicks on the element with the given `id`. (Android 4.3+)
- `Boolean longclickByIdAndIndex(String id, Number index)`
  Longclicks on the n-th element with the given `id`. (Android 4.3+)
- `Boolean check(String pattern)`
  Checks the element containing the given glob `pattern`.
- `Boolean check(Number x, Number y)`
  Checks the element at the specified location.
- `Boolean checkById(String id, Number index)`
  Checks the element with the given `id`. (Android 4.3+)
- `Boolean checkByIdAndIndex(String id, Number index)`
  Checks the n-th element with the given `id`. (Android 4.3+)
- `Boolean isChecked(String pattern)`
  Tests whether the element containing the given glob `pattern` is checked.
- `Boolean isChecked(Number x, Number y)`
  Tests whether the element at the specified location is checked.
- `Boolean isCheckedById(String id)`
  Tests whether the element with the given `id` is checked. (Android 4.3+)
- `Boolean isCheckedByIdAndIndex(String id, Number index)`
  Tests whether the n-th element with the given `id` is checked. (Android 4.3+)
- `Boolean uncheck(String pattern)`
  Unchecks the element containing the given glob `pattern`.
- `Boolean uncheck(Number x, Number y)`
  Unchecks the element at the specified location.
- `Boolean uncheckById(String id)`
  Unchecks the element with the given `id`. (Android 4.3+)
- `Boolean uncheckByIdAndIndex(String id, Number index)`
  Unchecks the n-th element with the given `id`. (Android 4.3+)
- `Boolean scrollForward(String pattern)`
  Scrolls the element containing the given glob `pattern`.
- `Boolean scrollForward(Number x, Number y)`
  Scrolls the element at the specified location.
- `Boolean scrollForwardById(String id)`
  Scrolls the element with the given `id`. (Android 4.3+)
- `Boolean scrollForwardByIdAndIndex(String id, Number index)`
  Scrolls the n-th element with the given `id`. (Android 4.3+)
- `Boolean scrollBackward(String pattern)`
  Scrolls the element containing the given glob `pattern`.
- `Boolean scrollBackward(Number x, Number y)`
  Scrolls the element at the specified location.
- `Boolean scrollBackwardById(String id)`
  Scrolls the element with the given `id`. (Android 4.3+)
- `Boolean scrollBackwardByIdAndIndex(String id, Number index)`
  Scrolls the n-th element with the given `id`. (Android 4.3+)
- `Boolean select(String pattern)`
  Selects the element containing the given glob `pattern`.
- `Boolean select(Number x, Number y)`
  Selects the element at the specified location.
- `Boolean selectById(String id)`
  Selects the element with the given `id`. (Android 4.3+)
- `Boolean selectByIdAndIndex(String id, Number index)`
  Selects the n-th element with the given `id`. (Android 4.3+)
- `Boolean clearSelection(String pattern)`
  Unselects the element containing the given glob `pattern`.
- `Boolean clearSelection(Number x, Number y)`
  Unselects the element at the specified location.
- `Boolean clearSelectionById(String id)`
  Unselects the element with the given `id`. (Android 4.3+)
- `Boolean clearSelectionByIdAndIndex(String id, Number index)`
  Unselects the n-th element with the given `id`. (Android 4.3+)
- `Boolean focus(String pattern)`
  Focuses the element containing the given glob `pattern`.
- `Boolean focus(Number x, Number y)`
  Focuses the element at the specified location.
- `Boolean focusById(String id)`
  Focuses the element with the given `id`. (Android 4.3+)
- `Boolean focusByIdAndIndex(String id, Number index)`
  Focuses the n-th element with the given `id`. (Android 4.3+)
- `Boolean expand(String pattern)`
  Expands the element containing the given glob `pattern`. (Android 4.4+)
- `Boolean expand(Number x, Number y)`
  Expands the element at the specified location. (Android 4.4+)
- `Boolean expandById(String id)`
  Expands the element with the given `id`. (Android 4.4+)
- `Boolean expandByIdAndIndex(String id, Number index)`
  Expands the n-th element with the given `id`. (Android 4.4+)
- `Boolean collapse(String pattern)`
  Collapses the element containing the given glob `pattern`. (Android 4.4+)
- `Boolean collapse(Number x, Number y)`
  Collapses the element at the specified location. (Android 4.4+)
- `Boolean cut()`
  Cuts the text of the focused element. (Android 4.3+)
- `Boolean cut(String pattern)`
  Cuts the text of the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean cut(Number x, Number y)`
  Cuts the text of the element at the specified location. (Android 4.3+)
- `Boolean cutById(String id)`
  Cuts the text of the element with the given `id`. (Android 4.3+)
- `Boolean cutByIdAndIndex(String id, Number index)`
  Cuts the text of the n-th element with the given `id`. (Android 4.3+)
- `Boolean copy()`
  Copies the text of the focused element. (Android 4.3+)
- `Boolean copy(String pattern)`
  Copies the text of the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean copy(Number x, Number y)`
  Copies the text of the element at the specified location. (Android 4.3+)
- `Boolean copyById(String id)`
  Copies the text of the element with the given `id`. (Android 4.3+)
- `Boolean copyByIdAndIndex(String id, Number index)`
  Copies the text of the n-th element with the given `id`. (Android 4.3+)
- `Boolean paste()`
  Pastes text to the focused element. (Android 4.3+)
- `Boolean paste(String pattern)`
  Pastes text to the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean paste(Number x, Number y)`
  Pastes text to the element at the specified location. (Android 4.3+)
- `Boolean pasteById(String id)`
  Pastes text to the element with the given `id`. (Android 4.3+)
- `Boolean pasteByIdAndIndex(String id, Number index)`
  Pastes text to the n-th element with the given `id`. (Android 4.3+)
- `Boolean setSelection2(Number start, Number end)`
  Sets the selection of the focused element to the defined range. (Android 4.3+)
- `Boolean setSelection2(String pattern, Number start, Number end)`
  Sets the selection of the element containing the given glob `pattern`. (Android 4.3+)
- `Boolean setSelection2(Number x, Number y, Number start, Number end)`
  Sets the selection of the element at the specified location. (Android 4.3+)
- `Boolean setSelection2ById(String id, Number start, Number end)`
  Sets the selection of the element with the given `id`. (Android 4.3+)
- `Boolean setSelection2ByIdAndIndex(String id, Number index, Number start, Number end)`
  Sets the selection of the n-th element with the given `id`. (Android 4.3+)
- `Boolean dismiss(String pattern)`
  Dismisses the element containing the given glob `pattern`. (Android 4.4+)
- `Boolean dismiss(Number x, Number y)`
  Dismisses the element at the specified location. (Android 4.4+)
- `Boolean dismissById(String id)`
  Dismisses the element with the given `id`. (Android 4.4+)
- `Boolean dismissByIdAndIndex(String id, Number index)`
  Dismisses the n-th element with the given `id`. (Android 4.4+)
- `String getText()`
  Returns the text of the focused element.
- `String getText(String pattern)`
  Returns the text of the element containing the given glob `pattern`.
- `String getText(Number x, Number y)`
  Returns the text of the element at the specified location.
- `String getTextById(String id)`
  Returns the text of the element with the given `id`. (Android 4.3+)
- `String getTextByIdAndIndex(String id, Number index)`
  Returns the text of the n-th element with the given `id`. (Android 4.3+)
- `String getContentDescription()`
  Returns the content description of the focused element.
- `String getContentDescription(String pattern)`
  Returns the content description of the element containing the given glob `pattern`.
- `String getContentDescription(Number x, Number y)`
  Returns the content description of the element at the specified location.
- `String getContentDescriptionById(String id)`
  Returns the content description of the element with the given `id`. (Android 4.3+)
- `String getContentDescriptionByIdAndIndex(String id, Number index)`
  Returns the content description of the n-th element with the given `id`. (Android 4.3+)
- `String getTextInActiveWindow()`
  Returns the text of all text elements. The order of the text elements can differ from the visual position.
- `String getContentDescriptionInActiveWindow()`
  Returns the content description of all elements. The order of the text elements can differ from the visual position.
- `Boolean setText2(String pattern, String text)`
  Sets the text of the element containing the given glob `pattern`. (Android 5+)
- `Boolean setText2(Number x, Number y, String text)`
  Sets the text of the element at the specified location. (Android 5+)
- `Boolean setText2ById(String id, String text)`
  Sets the text of the element with the given `id`. (Android 5+)
- `Boolean setText2ByIdAndIndex(String id, Number index, String text)`
  Sets the text of the n-th element with the given `id`. (Android 5+)
- `List getBounds(String pattern)`
  Returns the bounds of the element containing the given glob `pattern` in a list with the values [x, y, width, height].
- `List getBoundsById(String id)`
  Returns the bounds of the element with the given `id` in a list with the values [x, y, width, height]. (Android 4.3+)
- `List getBoundsByIdAndIndex(String id, Number index)`
  Returns the bounds of the n-th element with the given `id` in a list with the values [x, y, width, height]. (Android 4.3+)
- `Boolean existsElementById(String id)`
  Returns true when the element with the given `id` exists on the current window. (Android 4.3+)
- `Boolean existsElementByIdAndIndex(String id, Number index)`
  Returns true when the n-th element with the given `id` exists on the current window. (Android 4.3+)
- `Number getNumberOfElementsWithId(String id)`
  Returns number of elements with the defined `id` on the current window. (Android 4.3+)
- `Boolean sendKey(Number keyCode)`
  Simulates the specified key (Automagic input method required).
- `Boolean sendKey(String keyCodeName)`
  Simulates the specified key (Automagic input method required).
- `Boolean sendKey(String keyCodeName, String metaKey, ...)`
  Simulates the specified key with meta key state (Automagic input method required).
- `Boolean sendText(String text)`
  Sends the text to the focused component (Automagic input method required).
- `Boolean setText(String text)`
  Sets the text of the focused component (Automagic input method required).
- `Boolean setSelection(Number start, Number end)`
  Sets the selection of the focused component (Automagic input method required).
- `List getSelection()`
  Returns the start and end position of the cursor in a list with the values [start, end] (Automagic input method required).
- `Boolean selectAll()`
  Selects the text of the focused component (Automagic input method required).

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
