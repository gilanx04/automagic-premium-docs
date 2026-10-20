---
title: "Action - HTTP Request"
source: https://automagic4android.com/action_http_request_en.html
archived: 2022-10-06
archive_url: https://web.archive.org/web/20221006150209/https://automagic4android.com/action_http_request_en.html
category: action
---

# Action - HTTP Request

The action **HTTP Request** requests a resource from a server using the specified HTTP request method.

Note: This action is meant to be used for technical requests (REST and the like) and to process the response using scripts. If you simply want to download a file please use the action *Download URL*.
The action terminates with a status code of -1 for general errors. It will terminate with an error when not even a connection to the server can be established (network not available, IP can not be resolved etc.). Use an Exception-connection to handle such errors.

Examples:

- Fetch a web page of a weather service and test if it contains the word *rain*.
- Get the price of a product from an online retailers REST service.

### Settings

#### URL

The URL to request. [Variables are supported.](action_script.md#string-inline-expressions)
Examples:

- `http://example.com/weather.html?ts={triggertime,dateformat,yyyyMMdd}` becomes `http://example.com/weather.html?ts=20110213`

#### Verify certificates (https)

Whether certificates should be checked or not. Can be useful to ignore errors for self-signed certificates.

#### Authentication

Whether username and password should be passed to the server using basic authentication.

#### Username

The username to pass to the server. [Variables are supported.](action_script.md#string-inline-expressions)

#### Password

The password to pass to the server. [Variables are supported.](action_script.md#string-inline-expressions)

#### Client certificate

If a client certificate should be used.

#### Client certificate path

Path to the PKCS#12 file. [Variables are supported.](action_script.md#string-inline-expressions)

#### Client certificate password

The password to access the client certificate. [Variables are supported.](action_script.md#string-inline-expressions)

#### Network Type

Whether to use the currently available default network or send the request on the WiFi or cellular network.

#### Request Method

The HTTP request method to use. Not all methods are supported by all devices.

#### Content Type

The content type to use in the request as header Content-Type. [Variables are supported.](action_script.md#string-inline-expressions)

#### Form Field List

Comma separated list with key=value to send as `application/x-www-form-urlencoded` to the server. The values are automatically URL encoded. [Variables are supported.](action_script.md#string-inline-expressions)

Example: `Firstname=Hugo,Lastname=Habicht`

#### Data

The text data to send to the server. [Variables are supported.](action_script.md#string-inline-expressions)

#### Form Field Name

The name of the form field to use for the uploaded file. [Variables are supported.](action_script.md#string-inline-expressions)

#### File to upload

The path of the file to upload. The filename for the request is automatically determined based on the specified file. [Variables are supported.](action_script.md#string-inline-expressions)

#### Timeout

The timeout to use.

#### Custom HTTP Headers

A text containing the custom HTTP headers to send. [Variables are supported.](action_script.md#string-inline-expressions)

Each line should start with the header name and a colon followed by the value to send.

Examples:

- `User-Agent: my own user agent`
- `SOAPAction: "test"`

#### Store response in a variable or file

Whether to store the response in a variable or a file.

#### Variable

The name of the variable to store the response in. The response is converted to a string. [Variables are supported.](action_script.md#string-inline-expressions)

Warning: Responses larger than 1MB are not supported in a variable.

#### Encoding

The encoding to use to read the response from the server. Leave empty to use the encoding as specified by the servers response.

#### File

The path to store the file in. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- name as declared in the field Variable — the response as string
- `status_code` — the numeric HTTP status code, -1 when a general error occurs
- `error_message` — error message when the request could not be executed and `status_code` is set to -1
- `header_*` —
  All values of the response headers. The name of the variable is built using the prefix `header_` and the name of the header by replacing dash with underscore and converting the name to lowercase.
  Examples:
  - Header `Accept` is stored in variable `header_accept`
  - Header `Accept-Encoding` is stored in variable `header_accept_encoding`Values of headers that are specified multiple times in the response are provided as a list.
  Headers leading to an invalid variable name are ignored.

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
