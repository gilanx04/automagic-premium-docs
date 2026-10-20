---
title: "Action - Set Lock Pattern State"
source: https://automagic4android.com/action_set_lock_pattern_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Lock Pattern State

The action **Set Lock Pattern State** enables or disables the system setting whether the lock pattern should be used as the screen lock.

Warning: This function requires root access, is not officially supported by Android and might not work on all devices.

Example:

- Deactivate the pattern lock at home

### Settings

#### Lock Pattern

Whether to enable or disable the lock pattern.

#### Method

- **Secure setting**: Changes the setting in the regular settings database of Android (Android 4.2 and below)
- **Database**: Directly accesses the database containing the lock settings (Android 4.3+)
- **Service**: Asks the system service to change the setting (Android 4.3+)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
