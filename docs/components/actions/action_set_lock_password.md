---
title: "Action - Set Lock PIN/Password"
source: https://automagic4android.com/action_set_lock_password_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Lock PIN/Password

The action **Set Lock PIN/Password** sets the PIN/Password of the screen lock or resets the screen lock.

The action can be used to deactivate the screen lock:

1. Important: Set the screen lock in the settings of Android to 'None'
2. activate the desired PIN/Password screen lock in the settings of Android
3. use the option 'Clear PIN/Password' in the action to disable the screen lock

Note: The procedure might not work on all Android versions. The screen lock will not be dismissed when the lock screen is currently showing on screen.

Starting with Android 7, you can only use the action to set the PIN/Password when no PIN/Password is set yet so you can no longer use the action to remove a PIN/Password, except when Automagic is set as the [device owner](../../reference/device-owner.md).

Examples:

- Deactivate the screen lock when you are connected to the WiFi at home.

### Settings

#### Clear or Set PIN/Password

Whether to set a PIN/Password or to clear the PIN/Password.

#### PIN or Password

Whether you want to set a PIN or a Password.

#### Manual or from Variable

Whether the PIN/password is defined within the action itself or whether the action should set the PIN/password contained in a variable at the time when the action is executed.

#### PIN

The PIN to set.

#### Password

The password to set.

#### Variable

The name of the variable containing the PIN/Password to use (at the time the action is executed).

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
