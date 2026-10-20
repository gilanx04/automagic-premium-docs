---
title: "Condition - Active Network Type"
source: https://automagic4android.com/condition_active_network_type_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Active Network Type

The condition **Active Network Type** checks if a network (usually WiFi or Mobile) is active and usable for data traffic.

Examples:

- Execute a download action only when the current active network is WiFi.

### Settings

#### Network Type

Defines for what network types the condition should be true

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](../actions/action_script.md#string-inline-expressions)

### Supplied Variables

- `network_type` — the network type as number (None=-1, Mobile=0, WiFi=1, WiMAX=6, Bluetooth=7, Ethernet=9)
- `network_type_name` — the name of the network as string like `WIFI` or `MOBILE`
- `network_subtype` — the network subtype as number
- `network_subtype_name` — the network subtype as number
- `network_state` — the network state (CONNECTING, CONNECTED, SUSPENDED, DISCONNECTING, DISCONNECTED, UNKNOWN)
- `network_detailed_state` — the detailed network state (IDLE, SCANNING, CONNECTING, AUTHENTICATING, OBTAINING\_IPADDR, CONNECTED, SUSPENDED, DISCONNECTING, DISCONNECTED, FAILED, BLOCKED, VERIFYING\_POOR\_LINK, CAPTIVE\_PORTAL\_CHECK)
- `network_extra_info` — additional info as string (like SSID), when available
- `network_reason` — the reason of a failure, when available

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
