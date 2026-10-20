---
title: "Trigger - K-9 Mail Received"
source: https://automagic4android.com/trigger_k9_mail_received_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - K-9 Mail Received

The trigger **K-9 Mail Received** is executed when [K-9 Mail](https://play.google.com/store/apps/details?id=com.fsck.k9) receives a mail.

Examples:

- Play an alert sound when you receive a mail from the boss.

### Settings

#### K9 Account List

The comma separated list of accounts to consider (case insensitive). Glob patterns (\*, ?) are supported.

#### Sender List

The comma separated list of sender mail addresses to consider (case insensitive). Glob patterns (\*, ?) are supported.

#### Subject List

The comma separated list of subjects to consider (case insensitive). Glob patterns (\*, ?) are supported.

#### Receiver List

The comma separated list of receiver mail addresses to consider (case insensitive). Glob patterns (\*, ?) are supported.

#### CC List

The comma separated list of CC-mail addresses to consider (case insensitive). Glob patterns (\*, ?) are supported.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `k9_account` — the K-9 Mail account of the mail
- `k9_folder` — the K-9 folder of the mail
- `k9_to` — the recipients of the mail
- `k9_from` — the sender of the mail
- `k9_from_self` — whether or not the mail was sent by yourself (only set on newer versions of K-9)
- `k9_subject` — the subject of the mail
- `k9_sent_date` — the date the mail has been sent
- `k9_cc` — the cc of the mail
- `k9_bcc` — the bcc of the mail

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
