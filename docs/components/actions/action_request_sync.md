---
title: "Action - Request Sync"
source: https://automagic4android.com/action_request_sync_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Request Sync

The action **Request Sync** starts the synchronisation process of one or multiple accounts or some parts of the accounts. The order and the exact timing of the synchronisation is controlled by Android.
The action does not wait for the synchronisation to finish.

Examples:

- Disable the automatic synchronisation to save battery but execute the synchronisation manually every hour between 8am and 8pm.

### Settings

#### Accounts

The accounts to synchronize in format *Type*:*Name*.
Glob patterns can be used to match multiple accounts. [Variables are supported.](action_script.md#string-inline-expressions)

- `*` synchronises all accounts
- `Google:*` synchronises all Google accounts

#### Authorities

The parts/databases of the accounts to synchronize. Specify a `*` to synchronize all parts of the account.
Glob patterns can be used to match multiple authorities. [Variables are supported.](action_script.md#string-inline-expressions)

- `*` synchronises all authorities of the specified accounts
- `com.android.calendar` synchronises all calendars of the specified accounts

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
