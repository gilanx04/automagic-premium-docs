---
title: "Action - Open URL in Browser"
source: https://automagic4android.com/action_open_browser_url_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Open URL in Browser

The action **Open URL in Browser** opens the browser with the specified URL.

Tip: The browser can also be used to download a file by using a URL pointing to a PDF or other downloadable file.

Examples:

- Open a news page every morning.
- Download a PDF every morning at 5am.

### Settings

#### URL

The url to open. [Variables are supported.](action_script.md#string-inline-expressions)

Tip: You can use a variable to open n URL that changes dynamically by date.

`http://test.com/newspaper_{triggertime,dateformat,yyyyMMdd}.pdf`

will be replaced to

`http://test.com/newspaper_20120123.pdf`

#### Use defined app

Whether to use a defined app to open the URL or to let the system choose the most appropriate app.

#### Package Name

The app to open the URL. [Variables are supported.](action_script.md#string-inline-expressions)

#### Class Name

The component inside the app to open the URL with. [Variables are supported.](action_script.md#string-inline-expressions)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
