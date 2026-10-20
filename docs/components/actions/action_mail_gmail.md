---
title: "Action - Mail with Gmail"
source: https://automagic4android.com/action_mail_gmail_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Mail with Gmail

The action **Mail with Gmail** sends a mail using your Gmail account.

Note: If you have enabled **2-step verification** in your Google account then you need to create an application specific password for login in the settings of your google account: <https://www.google.com/settings/security>

Examples:

- Forward every SMS as a mail to your inbox.
- Send your location every 30 minutes to your girlfriend.
- Send the new **Gleeo Time Tracker** backups to your inbox.

### Settings

#### Authentication

Whether to use an account available on the device (OAuth) or to enter an account name and password.

#### Mail Account

The account name to use like `xyz@gmail.com`. [Variables are supported.](action_script.md#string-inline-expressions)

#### Password

The password to your mail account. [Variables are supported.](action_script.md#string-inline-expressions)

Info: The password is stored encrypted on the internal device storage and is not part of the regular `flows.xml` file.

#### To

The mail address of the recipient. [Variables are supported.](action_script.md#string-inline-expressions)

#### Reply To

The address to send responses to. [Variables are supported.](action_script.md#string-inline-expressions)

#### Subject

The subject of the mail. [Variables are supported.](action_script.md#string-inline-expressions)

#### Body

The message body of the mail. [Variables are supported.](action_script.md#string-inline-expressions)

#### Body MIME Type

Whether the body should is HTML or should be interpreted as plain unformatted text.

#### Files to Attach

The comma separated list of files to attach. [Variables are supported.](action_script.md#string-inline-expressions)

Tip: Files stored in a list by action **Init Variable File List** can be formatted using `{files,listformat,comma}` to a comma separated list.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
