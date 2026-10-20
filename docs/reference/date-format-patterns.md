---
title: "Date Format Patterns"
source: https://automagic4android.com/automagic/1.38/onlinehelp/en/dateformat_patterns.html
archived: 2019-05-17
archive_url: https://web.archive.org/web/20190517124826/https://automagic4android.com/automagic/1.38/onlinehelp/en/dateformat_patterns.html
category: reference
---

# Date Format Patterns

| **Symbol** | **Meaning** | **Presentation** | **Example** |
| --- | --- | --- | --- |
| `D` | day in year | (Number) | 189 |
| `E` | day of week | (Text) | Tuesday |
| `F` | day of week in month | (Number) | 2 *(2nd Wed in July)* |
| `G` | era designator | (Text) | AD |
| `H` | hour in day (0-23) | (Number) | 0 |
| `K` | hour in am/pm (0-11) | (Number) | 0 |
| `L` | stand-alone month | (Text/Number) | July / 07 |
| `M` | month in year | (Text/Number) | July / 07 |
| `S` | fractional seconds | (Number) | 978 |
| `W` | week in month | (Number) | 2 |
| `X (Android 7+)` | time zone (ISO 8601) | (Timezone) | -08 / -0800 / -08:00 |
| `Z` | time zone (RFC 822) | (Timezone) | -0800 |
| `a` | am/pm marker | (Text) | PM |
| `u (Android 7+)` | day of week (1 = Monday, ..., 7 = Sunday) | (Number) | 2 |
| `c (deprecated)` | stand-alone day of week | (Text/Number) | Tuesday / 2 |
| `d` | day in month | (Number) | 10 |
| `h` | hour in am/pm (1-12) | (Number) | 12 |
| `k` | hour in day (1-24) | (Number) | 24 |
| `m` | minute in hour | (Number) | 30 |
| `s` | second in minute | (Number) | 55 |
| `w` | week in year | (Number) | 27 |
| `y` | year | (Number) | 2010 |
| `z` | time zone | (Timezone) | Pacific Standard Time |
| `'` | escape for text | (Delimiter) | 'Date=' |
| `''` | single quote | (Literal) | 'o''clock' |

Examples:
The examples use the date **27th of September 2013 14:15:37**.

| **Pattern** | **Result** |
| --- | --- |
| `dd.MM.yyyy` | 27.09.2013 |
| `dd.MM.yyyy HH:mm:ss` | 27.09.2013 14:15:37 |
| `dd.MM.yyyy HH:mm` | 27.09.2013 14:15 |
| `dd.MM.yyyy hh:mm a` | 27.09.2013 2:15 PM |
| `yyyy-MM-dd HH:mm:ss.SSS` | 2013-09-27 14:15:37.432 |
| `EEEE, dd'th' MMM yyyy` | Friday, 27th September 2013 |
| `'Week' w` | Week 39 |
| `'Day' D 'of the year' yyyy` | Day 270 of the year 2013 |

---

[← Indeks referensi](README.md) · [Peta dokumentasi](../README.md)
