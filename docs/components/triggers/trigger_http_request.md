---
title: "Trigger - HTTP Request (Experimental)"
source: https://automagic4android.com/trigger_http_request_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---

# Trigger - HTTP Request (Experimental)

The trigger **HTTP Request (Experimental)** is executed when a HTTP request is received using the specified path and port.

Note: The built-in webserver is neither fast nor should you try to upload large files. Please don't use it to run webshops, corporate websites or sites like Slashdot on your phone.

Examples:

- Send an SMS from your Phone using your PC when the URL `http://192.168.1.XX:8080/sms?receiver=12345&text=test` is requested.
- Return a page with the list of files on the SD card when the URL `http://192.168.1.XX:8080/files/xyz` is requested.

### Settings

#### Path

The path to handle by this trigger. Glob patterns (\*, ?) are supported.
Examples:

- `/automagic/test`
- `/automagic/files/*` to handle all paths that start with `/automagic/files/`

The trigger with the longest path is preferred when multiple triggers match requested path since only one response can be written.
Examples: The first trigger is preferred when two triggers with paths `/automagic/test` and `/automagic/*` are available.

#### Port

The port of the server.

#### Bind to WiFi interface only

Whether to listen for HTTP requests on all interfaces or just on the WiFi interface.

#### Keep WiFi awake

Whether to keep the WiFi radio awake, otherwise the WiFi radio might turn off to save battery and a connection to your device is no longer possible.

#### Finish HTTP Response

Whether to finish the HTTP response by sending an empty response to the client.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `triggertime` — the time the trigger executed
- `remote_host` — the name or IP of the remote host
- `remote_port` — the port of the remote host
- `request_path` — the decoded path of the request (e.g. `/automagic/test`)
- `method` — the HTTP method (e.g. GET, POST, PUT)
- `header_*` —
  All values of the headers. The name of the variable is built using the prefix `header_` and the name of the header by replacing dash with underscore and converting the name to lowercase.
  Examples:
  - Header `Accept` is stored in variable `header_accept`
  - Header `Accept-Encoding` is stored in variable `header_accept_encoding`Headers leading to an invalid variable name are ignored.
- `param_*` —
  All values of the request parameters. The name of the variable is built using the prefix `param_` and the name of the parameter by converting the name to lowercase.
  Example:
  - Parameter `test` is stored in variable `param_test`Parameters leading to an invalid variable name are ignored.
- `file_*` —
  All paths of the uploaded files. The name of the variable is built using the prefix `file_` and the name of the parameter by converting the name to lowercase.
  Example:
  - Parameter `File` is stored in a variable `file_file`Parameters leading to an invalid variable name are ignored.
- `http_headers` — Map containing all unmodified names and values of the received HTTP headers
- `http_params` — Map containing all unmodified names and values of the received HTTP parameters
- `http_files` — Map containing all unmodified form field names and paths to the uploaded files

---

[← Indeks Trigger](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
