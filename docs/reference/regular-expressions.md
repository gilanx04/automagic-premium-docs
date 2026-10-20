---
title: "Regular Expressions"
source: https://automagic4android.com/automagic/1.38/onlinehelp/en/regex_patterns.html
archived: 2019-05-17
archive_url: https://web.archive.org/web/20190517124904/https://automagic4android.com/automagic/1.38/onlinehelp/en/regex_patterns.html
category: reference
---

# Regular Expressions

Regular expressions can be used to test if a text contains a specific text or more general whether a given text matches a defined pattern.

Basic pattern examples:

| Pattern | Description |
| --- | --- |
| `Test.*` | This pattern matches a text that starts with Test with an unlimited number of successive characters, for example **Test**, **Testabc** but not **abcTest**, **123Test123** |
| `Test.+` | This pattern matches a text that starts with Test with an unlimited number of successive characters but must contain at least one character after `Test`. For example **TestX** but not **Test** |
| `[a-c]{3}` | This pattern matches a text that consists of exactly three characters a to c, for example: **aaa**, **abc**, **cba** but not **xyz**. |
| `\d{3}.*` | This pattern matches a text that starts with three digits, for example **123abc**, **123456** but not **12abc** or **abc123**. |

Automagic supports regular expressions with following functions in action *Script* or condition *Expression*:

- `Boolean matches(String s, String pattern)`
  Returns whether the string `s` matches the regular expression `pattern`.
- `Boolean matches(String s, String pattern, List groups)`
  Returns whether the string `s` matches the regular expression `pattern` and fills the captured groups into the existing list `groups`.
- `List findAll(String s, String pattern)`
  Returns a list of all matched values in `s` of regex `pattern`.
- `List findAll(String s, String pattern, boolean returnGroups)`
  Returns a list of all matched values in `s` of regex `pattern`. Optionally item consists of a list of the matched groups. (see [Regular expressions](regular-expressions.md))
- `String replaceAll(String s, String regex, String replacement)`
  Returns a modified string by replacing all substrings matching `regex` with `replacement` in string `s`.
- `List split(String s, String pattern)`
  Splits the string `s` into a list of strings by using the regular expression `pattern` as the delimiter.

## Examples for function `Boolean matches(String s, String pattern)`

- Test if a text contains the word **test**:
  `result = matches("this is a test", ".*test.*")`
- Test if a text contains at least three digits at the beginning:
  `result = matches("1234567", "\\d{3}.*")`
  The regular expression would only require one backslash by itself, but one backslash has to be escaped with one additional backslash in a string in a script of Automagic.

## Examples for function `Boolean matches(String s, String pattern, List groups)`

- Test if a text contains a number and store the first number in the list `groups`:
```
groups = newList();
result = matches("contact 123456 called", "\\D*(\\d*).*");
```

  The list `groups` will contain the two elements "contact 123456 called" and "123456".

## Examples for function `List findAll(String s, String pattern)`

- Returns a list of all matched values in `s` of regex `pattern`.:
  `result = findAll("contact 123456 calls at 8 o'clock", "\\d*");`
  The list `groups` will contain the two elements "123456" and "8".

## Examples for function `String replaceAll(String s, String regex, String replacement)`

- Remove all numbers from a text:
  `result = replaceAll("contact 123456 called", "\\d", "");`
  `result` will contain "contact called".
- Remove consecutive whitespace characters and replace with one space character:
  `result = replaceAll("a b c", "\\s+", " ");`
  `result` will contain "a b c".
- Separate the characters in a text by spaces:
  `result = replaceAll("1234567", "(.)", "$1 ");`
  `result` will contain "1 2 3 4 5 6 7 ".
  $1 refers to the text matched in the first capturing group enclosed by parenthesis.
- Insert different delimiters between characters:
  `result = replaceAll("123456", "(.)(.)", "$1/$2-");`
  `result` will contain "1/2-3/4-5/6-".
  $1 refers to the text matched in the first capturing group enclosed by parenthesis, $2 refers to the second capturing group enclosed by parenthesis.

## Examples for function `List split(String s, String pattern)`

- Split the text on every colon to create a list of tokens:
  `result = split("this:is:a:test", ":");`
  The list `result` will contain the four elements "this", "is", "a" and "test".
- Split a text into a list of words:
  `result = split("this is a:test", "\\W");`
  The list `result` will contain the four elements "this", "is", "a" and "test".

## Android regular expressions

Automagic uses the built-in classes of Android to support regular expressions. [Android API online documentation](http://developer.android.com/reference/java/util/regex/Pattern.html)

The following documentation is an extract of the most important features of the regular expression syntax.

## Escape sequences

| Column 1 | Column 2 |
| --- | --- |
| \ | Quote the following metacharacter (so `\.` matches a literal `.`). |
| \Q | Quote all following metacharacters until `\E`. |
| \E | Stop quoting metacharacters (started by `\Q`). |
| \\ | A literal backslash. |
| \u*hhhh* | The Unicode character U+hhhh (in hex). |
| \x*hh* | The Unicode character U+00hh (in hex). |
| \c*x* | The ASCII control character ^x (so `\cH` would be ^H, U+0008). |
| \a | The ASCII bell character (U+0007). |
| \e | The ASCII ESC character (U+001b). |
| \f | The ASCII form feed character (U+000c). |
| \n | The ASCII newline character (U+000a). |
| \r | The ASCII carriage return character (U+000d). |
| \t | The ASCII tab character (U+0009). |

## Character classes

It's possible to construct arbitrary character classes using set operations:

| Column 1 | Column 2 |
| --- | --- |
| [abc] | Any one of `a`, `b`, or `c`. (Enumeration.) |
| [a-c] | Any one of `a`, `b`, or `c`. (Range.) |
| [^abc] | Any character *except* `a`, `b`, or `c`. (Negation.) |
| [[a-f][0-9]] | Any character in either range. (Union.) |
| [[a-z]&&[jkl]] | Any character in both ranges. (Intersection.) |

Most of the time, the built-in character classes are more useful:

| Column 1 | Column 2 |
| --- | --- |
| \d | Any digit character (see note below). |
| \D | Any non-digit character (see note below). |
| \s | Any whitespace character (see note below). |
| \S | Any non-whitespace character (see note below). |
| \w | Any word character (see note below). |
| \W | Any non-word character (see note below). |
| \p{*NAME*} | Any character in the class with the given *NAME*. |
| \P{*NAME*} | Any character *not* in the named class. |

Note that these built-in classes don't just cover the traditional ASCII range. For example,
`\w` is equivalent to the character class `[\p{Ll}\p{Lu}\p{Lt}\p{Lo}\p{Nd}]`.
For more details see [Unicode TR-18](http://www.unicode.org/reports/tr18/#Compatibility_Properties),
and bear in mind that the set of characters in each class can vary between Unicode releases.
If you actually want to match only ASCII characters, specify the explicit characters you want;
if you mean 0-9 use `[0-9]` rather than `\d`, which would also include
Gurmukhi digits and so forth.

## Quantifiers

Quantifiers match some number of instances of the preceding regular expression.

| Column 1 | Column 2 |
| --- | --- |
| \* | Zero or more. |
| ? | Zero or one. |
| + | One or more. |
| {*n*} | Exactly *n*. |
| {*n,*} | At least *n*. |
| {*n*,*m*} | At least *n* but not more than *m*. |

Quantifiers are "greedy" by default, meaning that they will match the longest possible input
sequence. There are also non-greedy quantifiers that match the shortest possible input sequence.
They're same as the greedy ones but with a trailing `?`:

| Column 1 | Column 2 |
| --- | --- |
| \*? | Zero or more (non-greedy). |
| ?? | Zero or one (non-greedy). |
| +? | One or more (non-greedy). |
| {*n*}? | Exactly *n* (non-greedy). |
| {*n,*}? | At least *n* (non-greedy). |
| {*n*,*m*}? | At least *n* but not more than *m* (non-greedy). |

Quantifiers allow backtracking by default. There are also possessive quantifiers to prevent
backtracking. They're same as the greedy ones but with a trailing `+`:

| Column 1 | Column 2 |
| --- | --- |
| \*+ | Zero or more (possessive). |
| ?+ | Zero or one (possessive). |
| ++ | One or more (possessive). |
| {*n*}+ | Exactly *n* (possessive). |
| {*n,*}+ | At least *n* (possessive). |
| {*n*,*m*}+ | At least *n* but not more than *m* (possessive). |

## Zero-width assertions

| Column 1 | Column 2 |
| --- | --- |
| ^ | At beginning of line. |
| $ | At end of line. |
| \A | At beginning of input. |
| \b | At word boundary. |
| \B | At non-word boundary. |
| \G | At end of previous match. |
| \z | At end of input. |
| \Z | At end of input, or before newline at end. |

## Look-around assertions

Look-around assertions assert that the subpattern does (positive) or doesn't (negative) match
after (look-ahead) or before (look-behind) the current position, without including the matched
text in the containing match. The maximum length of possible matches for look-behind patterns
must not be unbounded.

| Column 1 | Column 2 |
| --- | --- |
| (?=*a*) | Zero-width positive look-ahead. |
| (?!*a*) | Zero-width negative look-ahead. |
| (?<=*a*) | Zero-width positive look-behind. |
| (?<!*a*) | Zero-width negative look-behind. |

## Groups

| Column 1 | Column 2 |
| --- | --- |
| (*a*) | A capturing group. |
| (?:*a*) | A non-capturing group. |
| (?>*a*) | An independent non-capturing group. (The first match of the subgroup is the only match tried.) |
| \*n* | The text already matched by capturing group *n*. |

See `group()` for details of how capturing groups are numbered and accessed.

## Operators

| Column 1 | Column 2 |
| --- | --- |
| *ab* | Expression *a* followed by expression *b*. |
| *a*|*b* | Either expression *a* or expression *b*. |

## Flags

| Column 1 | Column 2 |
| --- | --- |
| (?dimsux-dimsux:*a*) | Evaluates the expression *a* with the given flags enabled/disabled. |
| (?dimsux-dimsux) | Evaluates the rest of the pattern with the given flags enabled/disabled. |

The flags are:

| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| `i` | `CASE_INSENSITIVE` | case insensitive matching |
| `d` | `UNIX_LINES` | only accept `'\n'` as a line terminator |
| `m` | `MULTILINE` | allow `^` and `$` to match beginning/end of any line |
| `s` | `DOTALL` | allow `.` to match `'\n'` ("s" for "single line") |
| `u` | `UNICODE_CASE` | enable Unicode case folding |
| `x` | `COMMENTS` | allow whitespace and comments |

---

[← Indeks referensi](README.md) · [Peta dokumentasi](../README.md)
