---
title: "Action - Write HTTP Response File (Experimental)"
source: https://automagic4android.com/action_write_http_response_file_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Write HTTP Response File (Experimental)

The action **Write HTTP Response File (Experimental)** writes the specified file as a response to a HTTP request. The flow must be invoked by a trigger *HTTP Request* to write a response.

Example:

- Fetch a file on your Android device from your desktop PC when connected to the same WiFi network.

### Settings

#### File

The name of the file to deliver. [Variables are supported.](action_script.md#string-inline-expressions)

#### Custom HTTP Headers

A text containing the custom HTTP headers to send. [Variables are supported.](action_script.md#string-inline-expressions)

Each line should start with the header name and a colon followed by the value to send.

Examples:

- `User-Agent: my own user agent`
- `SOAPAction: "test"`

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
