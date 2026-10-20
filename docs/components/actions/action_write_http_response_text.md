---
title: "Action - Write HTTP Response Text (Experimental)"
source: https://automagic4android.com/action_write_http_response_text_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Write HTTP Response Text (Experimental)

The action **Write HTTP Response Text (Experimental)** writes the specified text as a response to a HTTP request. The flow must be invoked by a trigger *HTTP Request* to write a response.

Example:

- Return a page with device information when a specific page is requested.

### Settings

#### Text

The text to write. [Variables are supported.](action_script.md#string-inline-expressions)

#### Content Type

The content type (like text/plain or text/html) of the content. The content type is only considered when no data has been returned to the client yet. [Variables are supported.](action_script.md#string-inline-expressions)

#### Custom HTTP Headers

A text containing the custom HTTP headers to send. [Variables are supported.](action_script.md#string-inline-expressions)

Each line should start with the header name and a colon followed by the value to send.

Examples:

- `User-Agent: my own user agent`
- `SOAPAction: "test"`

#### Finish HTTP Response

Whether to finish the HTTP response by sending the text immediately to the client.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
