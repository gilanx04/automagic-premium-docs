---
title: "Action - Set Auto Sync State"
source: https://automagic4android.com/action_set_auto_sync_state_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Set Auto Sync State

The action **Set Auto Sync State** turns the automatic synchronisation on or off.

Examples:

- Turn the automatic synchronisation off at night.
- Turn off the automatic synchronisation of the company account on weekends.

### Settings

#### Auto Sync

Whether to turn auto sync on or off.

#### Global or Specific

Whether to change the auto sync globally or only for a the specified accounts/authorities. Changing the global switch does not change the settings of the individual accounts/authorities.

#### Accounts

The accounts to change in format *Type*:*Name*.
Glob patterns can be used to match multiple accounts. [Variables are supported.](action_script.md#string-inline-expressions)

- `*` changes all accounts
- `Google:*` changes all Google accounts

#### Authorities

The parts/databases of the accounts to change. Specify a `*` to change all parts of the account.
Glob patterns can be used to match multiple authorities. [Variables are supported.](action_script.md#string-inline-expressions)

- `*` changes all authorities of the specified accounts
- `com.android.calendar` changes all calendars of the specified accounts

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
