---
title: "Number Format Patterns"
source: https://automagic4android.com/automagic/1.38/onlinehelp/en/numberformat_patterns.html
archived: 2019-05-17
archive_url: https://web.archive.org/web/20190517133644/https://automagic4android.com/automagic/1.38/onlinehelp/en/numberformat_patterns.html
category: reference
---

# Number Format Patterns

| Symbol | Location | Localized? | Meaning |
| --- | --- | --- | --- |
| `0` | Number | Yes | Digit. |
| `@` | Number | No | Significant digit. |
| `#` | Number | Yes | Digit, leading zeroes are not shown. |
| `.` | Number | Yes | Decimal separator or monetary decimal separator. |
| `-` | Number | Yes | Minus sign. |
| `,` | Number | Yes | Grouping separator. |
| `E` | Number | Yes | Separates mantissa and exponent in scientific notation. *Does not need to be quoted in prefix or suffix.* |
| `+` | Exponent | Yes | Prefix positive exponents with localized plus sign. *Does not need to be quoted in prefix or suffix.* |
| `;` | Subpattern boundary | Yes | Separates positive and negative subpatterns. |
| `%` | Prefix or suffix | Yes | Multiply by 100 and show as percentage. |
| `‰` (`\u2030`) | Prefix or suffix | Yes | Multiply by 1000 and show as per mille. |
| `¤` (`\u00A4`) | Prefix or suffix | No | Currency sign, replaced by currency symbol. If doubled, replaced by international currency symbol. If present in a pattern, the monetary decimal separator is used instead of the decimal separator. |
| `'` | Prefix or suffix | No | Used to quote special characters in a prefix or suffix, for example, `"'#'#"` formats 123 to `"#123"`. To create a single quote itself, use two in a row: `"# o''clock"`. |
| `*` | Prefix or suffix boundary | Yes | Pad escape, precedes pad character. |

Examples:
The example use the number **1234.567**.

| **Pattern** | **Result** |
| --- | --- |
| `0.00` | 1234.57 |
| `0.00000` | 1234.56700 |
| `0.00###` | 1234.567 |
| `#,###` | 1,234 |

---

[← Indeks referensi](README.md) · [Peta dokumentasi](../README.md)
