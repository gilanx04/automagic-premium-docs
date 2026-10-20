---
title: "Action - Script"
source: https://automagic4android.com/action_script_en.html
archived: 2023-11-26
archive_url: https://web.archive.org/web/20231126151521/https://automagic4android.com/action_script_en.html
category: action
---

# Action - Script

The action **Script** executes a script doing some simple calculations and can be used to modify variables.

## Script Description

## Reserved Keywords

Following list of keywords are reserved and are therefore not allowed to be used as a variable name:
```
 abstract alias and AND assert
    boolean break byte
    case catch char class const continue
    def default do double
    else elsif ensure enum extends
    false final finally float for
    goto
    if implements import in instanceof int interface
    long
    mod
    native new next not NOT null
    or OR
    package private protected public
    redo repeat rescue retry return
    self short static strictfp super switch synchronized
    then this throw throws to transient true try
    undef unless until
    void volatile
    when while
    xor XOR
    yield
```

Only a few of the reserved keywords are currently used but are reserved for future extensions of the scripting language.

## Comments

Scripts can contain comments that are not executed when the script is interpreted.

- text after `//` to the end of the line
- text between `/*` and `*/`. Such a comment can also span multiple lines.

Examples:
```
    a=1+2;//this is a comment
    b=a+3;
    c=b+a;
    /* this is a
        multiline comment */
    d=c*2;
```

## Variables

A value like a number or a string can be stored in a variable using the assignment operator `=`
Variable names are case sensitive. A variable name has to start with a letter, a currency symbol (such as "$") or a connecting punctuation character (such as "\_"). The rest of the variable name can also contain digits. Unicode characters are supported, but it is highly recommended to use US-ASCII characters.

Examples:
```
    a = 3;//assign the number three to the variable a
    b = a;//assign the value stored in variable a to the variable b
```

There exist two types of variable scopes:

### Flow Local

Every variable declared in a script, expression or inline script is by default flow local as long as the name of the variable does not start with `global_`.

Examples of flow local variables with a value assigned:

- `a = 1;`   number one stored in a variable called 'a'
- `var1 = 1.234;`   decimal number 1.234 stored in a variable called 'var1'
- `var_123 = "Hello World";`   string "Hello World" stored in a variable called 'var\_123'
- `_m = true;`   boolean value 'true' stored in a variable called '\_m'
- `var2 = a;`   stores the value stored in variable 'a' in a variable called 'var2'

### Global

Every variable that starts with `global_` is global and therefore accessible by other flows and will also be persisted to the external memory and reloaded when you stop/restart the Automagic service.

Examples of global variables with a value assigned:

- `global_a = 1;`   number one stored in a variable called 'global\_a'
- `global_var1 = 1.234;`   decimal number 1.234 stored in a variable called 'global\_var1'
- `global_var_123 = "Hello World";`   string "Hello World" stored in a variable called 'global\_var\_123'
- `global_m = true;`   boolean value 'true' stored in a variable called 'global\_m'

Variables are references to values (like a pointer). Assigning the value stored in a variable to another variable does not copy the value but both variables point to the exact same value.
This is especially important when modifiable values like lists are used.
Example:
```
    a = newList(1, 2, 3);
    b = a;
    //at this point both variables a and b point to the exact
    // same list (the list only exists once)
    addElement(a, 4);
    //the list now contains 1, 2, 3, 4
    //both variables a and b still point to the same list

    //both loops therefore print the values 1, 2, 3 and 4 in the log:
    for (x in a)
    {
        log("{x}");
    }

    for (x in b)
    {
        log("{x}");
    }
```

## Operators

Following operators are supported in expressions:

- `+`    addition and string concatenation
- `-`    subtraction
- `*`    multiplication
- `/`    division
- `%`    modulo division
- `<`    less than
- `<=`    less than or equal
- `>`    greater than
- `>=`    greater than or equal
- `==`    equal
- `!=`    not equal
- `AND`, `&&`    and
- `OR`, `||`    or
- `XOR`, `^`    exclusive or
- `NOT`, `!`    not (unary)

## Expressions

An expression is a construct made up of variables, operators and function calls, that evaluates to a single value.

Examples:

- `42`
- `1+2`
- `a=1`
- `b=a+1`
- `c=(a+1)*(b-3)`
- `global_a=1`
- `a=sqrt(9)`
- `b=addDays(triggertime, 3)`
- `c=replace("hello automagic", "automagic", "world")`
- `b=addDays(triggertime, sqrt(9))`
- `b="Hello " + "World"`
- `a=true`
- `b=false`
- `c=a AND b OR c>=5`
- `c=NOT a AND NOT b`

### String Inline Expressions

Inline expressions in strings can be used to replace a part of the string by a variable or expression. The rules described here also apply to the text fields of triggers, conditions and actions documented in the help page with Variables are supported.
An inline expression is enclosed in curly braces: `{expression}`

Example simple inline expressions:

- `var1="Test";
  var2="This is a {var1}";`
  'var2' will contain the string "This is a Test" after the script is evaluated
- `var="one plus two is {1 + 2}";`
  'var' is evaluated to "one plus two is 3"

Inline expressions can be formatted by defining a format type and depending on the format type a pattern to use: `{var,formattype,pattern}`

Example inline expressions with formatting:

- `var="Today is {getDate(),dateformat,dd.MM.yyyy}";`
  'var' will contain the string "Today is 21.07.2012"
- `var="It's {getDate(),dateformat,HH:mm}";`
  'var' will contain the string "It's 12:32"
- `var="It's {getDate(),dateformat,timezone,UTC,HH:mm}";`
  'var' will contain the string "It's 10:32"
- `var="Value: {1.456789,numberformat,0.00}";`
  'var' is evaluated to "Value: 1.46"
- `var="I'm here: {location,locationformat,decimal}";`
  'var' is evaluated to "I'm here: 46.76817,7.603751"
- `var="{files,listformat,comma}";`
  'var' is evaluated to "/mnt/sdcard/file1,/mnt/sdcard/file2"

Supported format types:

- `dateformat`: Formats the date using the specified date pattern. See [pattern characters](../../reference/date-format-patterns.md) for a description of the supported patterns.
  The optional sub-format `timezone` along with the name of the timezone can be used to define the timezone used to format the date/time. Accepted timezone names are either UTC, GMT or the Olson name of a timezone name of the form *Area/Location*, such as `America/Los_Angeles` (device dependent). GMT is used for unknown timezone names.
  Examples:
  - `{triggertime,dateformat,timezone,UTC,HH:mm}`
  - `{triggertime,dateformat,timezone,America/Los_Angeles,HH:mm}`
  - `{triggertime,dateformat,timezone,Europe/London,HH:mm}`
  - `{triggertime,dateformat,timezone,Europe/Paris,HH:mm}`
  - `{triggertime,dateformat,timezone,Africa/Harare,HH:mm}`
- `numberformat`: Formats the number using the specified decimal format. See [pattern characters](../../reference/number-format-patterns.md) for a description of the supported patterns.
- `locationformat`: Formats the address of the location when available in a single line of text when no format is specified. (Data connection is required)
  Following locationformat patterns are supported:
  - `multiline`: Formats the address as a multiline text. (Data connection is required)
  - `decimal`: Formats latitude,longitude as decimal numbers (+/-DDD.DDDDD). Example: 46.76817,7.603751.
  - `microdegrees`: Formats latitude,longitude multiplied by 1'000'000 as integers. Example: 46768355,7604022. This format can be useful in a call to a REST service.
  - `swiss`: Formats latitude,longitude converted to the [Swiss coordinate system](http://de.wikipedia.org/wiki/Schweizer_Landeskoordinaten).
- `listformat`: Formats the list of values as a multiline text with one item per line when no pattern is specified.
  Following listformat patterns are supported:
  - `comma`: Formats the list of values as a comma separated list.
  - `semicolon`: Formats the list of values as a semicolon separated list.
- `jsonformat`: Formats the value as JSON fragment.

Inline expressions in strings with single quotes are not interpreted. This can be helpful for regular expressions, where a quantifier like **{2}** in the pattern **([0-9]){2}.\*** should not be replaced with **2**.

Example:

- `var='Today is {getDate(),dateformat,dd.MM.yyyy}';`
  'var' is evaluated to 'Today is {getDate(),dateformat,dd.MM.yyyy}'

## Control Structures

### `if` Statement

An if statement can be used to evaluate a block of code when a condition is true.
Example:
```
    if (a<3)
    {
        b = 0;
    }
    else
    {
        b = 1;
    }
```

In this example variable `b` is assigned the value zero when the variable `a` contains a value less than 3, `b` is assigned the value one when the variable `a` contains a value greater or equal to 3.

### `for` Loop

A for loop evaluates a block of code for every value in a list of values.
Example:
```
    list=newList(1, 2, 3);

    for (a in list)
    {
        log("a contains {a}");
    }
```

This example would print the following output in the log:
```
    a contains 1
    a contains 2
    a contains 3
```

### Numeric List Creation Expression

Since it is very common to create a list containing a sequence of numeric values there is a shorthand to create such a list using `[<number> to <number>, <step size>]`:
Examples:
```
    list = [1 to 10];//without the optional step size

    for (a in list)
    {
        log(a);
    }
    //logs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    //inlined
    for (a in [1 to 10])
    {
        log(a);
    }
    //logs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    //inlined with step size of 2
    for (a in [1 to 10, 2])
    {
        log(a);
    }
    //logs 1, 3, 5, 7, 9

    //inlined with negative step size of -3
    for (a in [10 to 1, -3])
    {
        log(a);
    }
    //logs 10, 7, 4, 1
```

### Access to list and map entries

Single values of lists and maps can be accessed with brackets.
Examples:
```
    list = [1 to 10];
    a = list[0];//get first element of the list: 1
    a = list[1];//get second element of the list: 2

    list[2] = 999;//assigns 999 to the third element of the list

    map = newMap();
    map["key1"] = 1;//creates a map entry key1-->1
    map["key2"] = 2;//creates a map entry key2-->2

    a = map["key1"];//gets the value of entry with key1: 1
    a = map["key2"];//gets the value of entry with key2: 2
```

### `while` Loop

A while-loop evaluates a block of code as long as a condition is true.
Example:
```
    a = 0;

    while (a < 10)
    {
        log(a);
        a = a + 1;
    }
    //logs 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

### `return` statement

The return statement can be used to terminate a script early and optionally to return a given value.
Example:
```
    a = null;
    if (a == null)
    {
        return;
    }

    log("X");//not reached since return terminates the script
```

### `break` statement

The break statement can be used to terminate a loop and to continue the script after the loop body.
Example:
```
    for (a in [1 to 10])
    {
        if (a == 4)
        {
            break;
        }
        log(a);
    }

    log("X");
    //logs 1, 2, 3, X
```

### `continue` statement

The continue statement can be used to immediately continue with the next iteration of the loop.
Example:
```
    for (a in [1 to 10])
    {
        if (a == 4)
        {
            continue;
        }
        log(a);
    }

    log("X");
    //logs 1, 2, 3, 5, 6, 7, 8, 9, 10, X
```

## Functions

Built in functions can be called to calculate trigonometric values, create lists, extract values from an XML and much more.
Examples:
```
    a = sin(1.2);//evaluates to 0.932039...
    a = max(1, 2, 3, 4, 5);//evaluates to 5
    a = isEmpty([1 to 10]);//evaluates to false
    a = containsElement([1 to 10, 2], 3);//evaluates to true
```

Tip: Please also see the [Script examples](../../reference/script-examples.md) page that shows some commonly used script snippets.

- `Object convertNull(Object value, Object defaultValue)`
  Returns the value of the first argument or returns `default` when the value is null.
- `Number abs(Number value)`
  Returns the absolute value of `value`.
- `Number pow(Number base, Number exponent)`
  Returns the value of the first argument raised to the power of the second argument.
- `Number sqrt(Number a)`
  Returns the square root of the number.
- `Number sin(Number a)`
  Returns the sine of the angle in radians.
- `Number cos(Number a)`
  Returns the cosine of the angle in radians.
- `Number tan(Number a)`
  Returns the tangent of the angle in radians.
- `Number asin(Number a)`
  Returns the sine of the angle in radians.
- `Number acos(Number a)`
  Returns the arc cosine of the angle in radians.
- `Number atan(Number a)`
  Returns the arc tangent of the angle in radians.
- `Number atan2(Number y, Number x)`
  Returns the angle of the polar representation of the rectangular coordinate (x, y).
- `Number sinh(Number a)`
  Returns the hyperbolic sine of the value.
- `Number cosh(Number a)`
  Returns the hyperbolic cosine of the value.
- `Number tanh(Number a)`
  Returns the hyperbolic tangent of the value.
- `Number log10(Number a)`
  Returns the base 10 logarithm of the value.
- `Number ln(Number a)`
  Returns the natural logarithm (base *e*) of the value.
- `Number toRadians(Number a)`
  Converts the Number from degrees to radians.
- `Number toDegrees(Number a)`
  Converts the Number from radians to degrees.
- `Number round(Number a)`
  Rounds the number to the nearest integer.
- `Number ceil(Number a)`
  Returns the next highest integer value by rounding up value if necessary.
- `Number floor(Number a)`
  Returns the next lowest integer value by rounding down value if necessary.
- `Date addDays(Date d, Number a)`
  Returns a new date by adding `a` number of days to the date `d`.
- `Date addHours(Date d, Number a)`
  Returns a new date by adding `a` number of hours to the date `d`.
- `Date addMinutes(Date d, Number a)`
  Returns a new Date by adding `a` number of minutes to the date `d`.
- `Date addSeconds(Date d, Number a)`
  Returns a new date by adding `a` number of seconds to the date `d`.
- `Date getDate()`
  Returns the current date and time.
- `Date getDate(String date, String pattern)`
  Converts the string to a date using the specified pattern. (see [pattern characters](../../reference/date-format-patterns.md))
- `Date getDate(Number year, Number month, Number day)`
  Returns the Date specified by the arguments.
- `Date getDate(Number year, Number month, Number day, Number hours, Number minutes, Number seconds)`
  Returns the date specified by the arguments.
- `Date getDate(Date date, Number hours, Number minutes, Number seconds)`
  Returns the date specified by the arguments.
- `Date getDate(Date date, Number hours, Number minutes, Number seconds, String timezone)`
  Returns the date specified by the arguments in the defined timezone.
- `Number getUptimeMillis()`
  Returns milliseconds since boot, not counting time spent in deep sleep.
- `Number getElapsedRealtimeMillis()`
  Returns milliseconds since boot, including time spent in sleep.
- `Number getDurationMillis(String duration)`
  Returns the duration in milliseconds specified by the duration string (e.g. "2m 15s" returns 135000).
- `String getDurationString(Number duration)`
  Returns the duration string representing the specified milliseconds (e.g. 135000 returns "2m 15s").
- `Number getByteSize(String byteSize)`
  Returns the number of bytes specified by the string (e.g. "10kb 15b" returns 10255).
- `String getByteSizeString(Number byteSize)`
  Returns the formatted byte string representing the specified bytes (e.g. 10255 returns "10kb 15b").
- `Number toNumber(String number)`
  Converts the specified parameter to a number.
- `Number min(Number n1, Number n2, ...)`
  Returns the smallest number of the arguments.
- `Number max(Number n1, Number n2, ...)`
  Returns the largest number of the arguments.
- `Boolean isEmpty(String s)`
  Returns whether the string is empty or not.
- `Number length(String s)`
  Returns the number of characters in string `s`.
- `String substring(String s, Number start, Number end)`
  Returns the substring of the specified string.
- `String substring(String s, Number start)`
  Returns the substring starting at the specified index.
- `String left(String s, Number length)`
  Returns the first `length` characters of the specified string.
- `String right(String s, Number length)`
  Returns the last `length` characters of the specified string.
- `Number indexOf(String s, String search)`
  Returns the first index of `search` in `s`.
- `Number indexOf(String s, String search, Number start)`
  Returns the first index of `search` after `start` in `s`.
- `Number lastIndexOf(String s, String search)`
  Returns the last index of `search` in `s`.
- `Number lastIndexOf(String s, String search, Number start)`
  Returns the last index of `search` before `start` in `s`.
- `Boolean startsWith(String s, String prefix)`
  Checks whether the string `s` starts with `prefix`.
- `Boolean endsWith(String s, String suffix)`
  Checks whether the string `s` ends with `suffix`.
- `Boolean contains(String s, String search)`
  Checks whether the string `s` contains the substring `search`.
- `List split(String s, String pattern)`
  Splits the string `s` into a list of strings by using the regular expression `pattern` as the delimiter. (see [Regular expressions](../../reference/regular-expressions.md))
- `List splitCSVRecord(String s)`
  Splits the comma delimited string `s` into a list of tokens. Takes double quotes for escaped fields into consideration.
- `List splitCSVRecords(String s)`
  Splits multiple lines of a comma delimited string `s` into a list (per line) of list of tokens. Takes double quotes for escaped fields into consideration.
- `String join(List list, String delimiter)`
  Joins the elements of the list into a string by separating the elements with the specified `delimiter`.
- `Boolean matches(String s, String pattern)`
  Returns whether the string `s` matches the regular expression `pattern`. (see [Regular expressions](../../reference/regular-expressions.md))
- `Boolean matches(String s, String pattern, List groups)`
  Returns whether the string `s` matches the regular expression `pattern` and fills the captured groups into the existing list `groups`. (see [Regular expressions](../../reference/regular-expressions.md))
- `List findAll(String s, String pattern)`
  Returns a list of all matched values in `s` of regex `pattern`. (see [Regular expressions](../../reference/regular-expressions.md))
- `List findAll(String s, String pattern, boolean returnGroups)`
  Returns a list of all matched values in `s` of regex `pattern`. Optionally item consists of a list of the matched groups. (see [Regular expressions](../../reference/regular-expressions.md))
- `String replace(String s, String search, String replace)`
  Returns a modified string by replacing all occurrences of `search` with `replace` in string `s`.
- `String replaceAll(String s, String regex, String replacement)`
  Returns a modified string by replacing all substrings matching `regex` with `replacement` in string `s`. (see [Regular expressions](../../reference/regular-expressions.md))
- `String trim(String s)`
  Returns a modified string by removing all leading and trailing whitespace from string `s`.
- `String concat(Object o1, ...)`
  Returns the string concatenation of the specified objects.
- `String toUpperCase(String s)`
  Converts the string to upper case using the rules of the default locale.
- `String toLowerCase(String s)`
  Converts the string to lower case using the rules of the default locale.
- `String encodeURLForm(String urlPart)`
  URL-encodes the specified `urlPart` (for application/x-www-form-urlencoded, spaces are encoded as +).
- `String encodeURL(String urlPart)`
  URL-encodes the specified `urlPart` (spaces are encoded as %20).
- `String encodeHTML(String text)`
  HTML-encodes the specified `text`.
- `List newList(Object o1, ...)`
  Returns a new list containing the specified objects.
- `List copyList(List list)`
  Returns a copy of specified list (flat copy).
- `Number length(List list)`
  Returns the number of elements in `list`.
- `Boolean isEmpty(List list)`
  Returns whether the list contains any elements or not.
- `List addElement(List list, Object o1)`
  Returns the same list after adding the object at the end of the list. Returns a new list when the list should not exist yet.
- `List addElement(List list, Number index, Object o1)`
  Returns the same list after adding the object at the specified index (zero based).
- `List addAllElements(List list, List elementsToAdd)`
  Returns the same list after adding all elements specified in list `elementsToAdd`.
- `List removeDuplicateElements(List list)`
  Returns the same list after removing all duplicates.
- `List removeElementValue(List list, Object o1)`
  Returns the same list after removing all elements with the specified value.
- `List removeAllElementValues(List list, List elementsToRemove)`
  Returns the same list after removing all elements contained in the second list.
- `Boolean containsElement(List list, Object o1)`
  Returns `true` when the list contains the specified element.
- `Object removeElement(List list, Number index)`
  Removes the object at the specified index (zero based) and returns the removed object.
- `List removeElements(List list, Number fromIndex, Number toIndex)`
  Removes the objects at the specified index range (zero based, [fromIndex,toIndex[) and returns the removed objects in a list.
- `Object getElement(List list, Number index)`
  Returns the object at the specified index (zero based).
- `List setElement(List list, Number index, Object value)`
  Sets the object at the specified index (zero based).
- `Object getRandomElement(List list)`
  Returns a random element of the list.
- `List shuffleList(List list)`
  Randomly shuffles the elements of the list.
- `Number indexOfElement(List list, Object value)`
  Returns the first index of the element in the list or -1 when the element is not contained in the list.
- `Number indexOfElement(List list, Object value, Number start)`
  Returns the first index of the element in the list that is bigger or equal to `start` or -1 when the element is not contained in the list.
- `List sort(List list, Boolean casesensitive, Boolean natural)`
  Modifies the list by sorting the values.
- `List reverse(List list)`
  Modifies the list by reversing the order of the contained values.
- `Map newMap()`
  Returns a new empty map
- `Map newMapFromValues(String key1, Object value1, ...)`
  Returns a new map initialized to contain the specified keys and values.
- `Boolean isEmpty(Map map)`
  Returns whether the map contains any elements or not.
- `Number length(Map map)`
  Returns the number of elements in `map`.
- `Map copyMap(Map map)`
  Returns a copy of specified map (flat copy).
- `Map addMapEntry(Map map, String key, Object value)`
  Adds a new entry `key->value` to the map and returns the map. Returns a new map when the map should not exist yet.
- `Map addAllMapEntries(Map map, Map entriesToAdd)`
  Adds all entries of the second map to the first map and returns the first map.
- `Object getMapValue(Map map, String key)`
  Returns the object for `key` or `null` when no mapping for key exists.
- `Object getMapValue(Map map, String key, Object default)`
  Returns the object for `key` or `default` when no mapping for key exists or `map` is null.
- `Object removeMapEntry(Map map, String key)`
  Removes the entry for the given `key` and returns the value.
- `List getMapKeys(Map map)`
  Returns a list of the keys of `map`.
- `List getMapValues(Map map)`
  Returns a list of the values of `map`.
- `String evaluateXPathAsString(String xml, String xpath)`
  Evaluates the XPath expression on the given XML and returns the result as a string. (see [XPath Specification](http://www.w3.org/TR/xpath/))
- `String hash(String value, String encoding, String algorithm)`
  Calculates the hash of `value` using the specified `encoding` (like `UTF-8` or `UTF-16LE`) and hashing `algorithm` (like `MD5` or `SHA1`).
- `String toJSON(Object value)`
  Converts the specified object to a JSON string.
- `String toJSON(Object value, Boolean indent)`
  Converts the specified object to a JSON string, indented or not.
- `Object fromJSON(String value)`
  Converts the specified JSON string into an object.
- `Object log(Object value)`
  Logs the specified object in the Automagic log and returns the unmodified object.
- `Object eval(String script)`
  Evaluates the string as a script and returns the value of the last expression.
- `Number random()`
  Returns a random number between 0.0 and 1.0 (exclusive).
- `Number random(Number low, Number high)`
  Returns a random number between `low` and `high` (inclusive).
- `Boolean sleep(Number milliseconds)`
  Waits for the specified amount of `milliseconds`.
- `Boolean sleep(String duration)`
  Waits for the specified `duration` like "2m 30s".
- `Boolean existsFile(String path)`
  Checks whether the file denoted by `path` exists or not.
- `Boolean isDirectory(String path)`
  Checks whether the file denoted by `path` is a directory.
- `String getExternalStorageDir()`
  Returns the path to the primary external storage directory.
- `Number getPixelColor(Bitmap image_data, Number x, Number y)`
  Returns the color (argb) of the pixel of the `image` at location `x`, `y`.
- `Number getRed(Number color)`
  Returns the red component of the specified `color`.
- `Number getGreen(Number color)`
  Returns the green component of the specified `color`.
- `Number getBlue(Number color)`
  Returns the blue component of the specified `color`.
- `Number getAlpha(Number color)`
  Returns the alpha component of the specified `color`.
- `Number newColor(Number a, Number r, Number g, Number b)`
  Returns a new color from the specified ARGB components.
- `Number distance(Location loc1, Location loc2)`
  Calculates the distance between locations `loc1` and `loc2` in meters.
- `Location newLocation(Number latitude, Number longitude)`
  Creates a new Location for the specified `latitude` and `longitude`.
- `String setHTTPResponseHeader(String header, String value)`
  Sets the HTTP response header to the specified value and returns the value.
- `Number setHTTPResponseStatus(Number status)`
  Sets the HTTP response status to the specified value and returns the value.
- `Boolean isList(Object value)`
  Returns whether the specified value is a List or not.
- `Boolean isMap(Object value)`
  Returns whether the specified value is a Map or not.
- `Boolean isString(Object value)`
  Returns whether the specified value is a String or not.
- `Boolean isNumber(Object value)`
  Returns whether the specified value is a Number or not.
- `Boolean isBoolean(Object value)`
  Returns whether the specified value is a Boolean or not.
- `Boolean isLocation(Object value)`
  Returns whether the specified value is a Location or not.
- `Object getWidgetElementProperty(String widgetName, String elementName, String property)`
  Gets the current value of the property of the specified widget element.
- `Object setWidgetElementProperty(String widgetName, String elementName, String property, Object value)`
  Sets the given property of the specified widget element to `value`.
- `Boolean refreshWidget(String widgetName, Boolean reloadImages)`
  Refreshes the widget and optionally also reloads images.
- `String getAppName(String packageName)`
  Returns the display name of the app from the specified package or null when not available.
- `String getActivityName(String packageName, String className)`
  Returns the display name of the activity from the specified package and class or null when not available.
- `String getServiceName(String packageName, String className)`
  Returns the display name of the service from the specified package and class or null when not available.
- `List getFlowNames()`
  Returns a list containing the names of all flows.
- `List getFlowNamesByGroup(String group)`
  Returns a list containing the names of the flows of the specified `group`.
- `List getFlowGroupNames()`
  Returns a list containing the names of the flow groups.
- `List getWidgetNames()`
  Returns a list containing the names of all widgets.
- `Map getFlowStatisticsDuration()`
  Returns a map of the executed flows. Key=Flow name, Value=total execution duration in milliseconds, sorted by value descending.
- `Map getFlowStatisticsCount()`
  Returns a map of the executed flows. Key=Flow name, Value=total execution count, sorted by value descending.
- `Boolean resetFlowStatistics()`
  Resets the flow statistics.
- `Object getValue(String name, Object default)`
  Returns the value of the variable named `name` or returns `default` when the variable is undefined or null.
- `Object setValue(String name, Object value)`
  Sets the variable named `name` to `value` and returns `value`
- `Object removeVariable(String name)`
  Removes the variable named `name`.
- `List getVariableNames()`
  Returns a list of all variables currently available (local and global).
- `Number getAndroidSDKVersion()`
  Returns the SDK version number of the Android framework. (see [Android API versions](https://source.android.com/source/build-numbers.html#platform-code-names-versions-api-levels-and-ndk-releases))
- `Object getContext()`
  Returns the context of the application.
- `Object callJavaStaticMethod(String className, String methodSignature, Object params, ...)`
  Calls the defined public static method of the defined class.
- `Object callJavaConstructor(String className, String constructorSignature, Object params, ...)`
  Calls the public constructor of the defined class.
- `Object callJavaMethod(Object obj, String className, String methodSignature, Object params, ...)`
  Calls the specified instance method on the defined object.
- `Object getJavaStaticField(String className, String fieldName)`
  Returns the value of the specified public static field.
- `Object setJavaStaticField(String className, String fieldName, Object value)`
  Sets the value of the specified public static field.
- `Object getJavaField(Object obj, String className, String fieldName)`
  Returns the value of the specified public instance field.
- `Object setJavaField(Object obj, String className, String fieldName, Object value)`
  Sets the value of the specified public instance field.

Note: Are you missing a function? Please let us know in the forum.

## Advanced Topics

Every executable expression in a script evaluates to a value. A block of code evaluates to the value produced by the last expression in the block and allows to create inline scripts with multiple expressions:
```
    s = "{a=1;b=2}";
    log(s);//logs 2

    a = true;
    b = if (a) 1 else 2;
    log(b);//logs 1

    for (a in [0 to 10])
    {
        log(if(a<5) "X" else "-");
    }
    //logs X, X, X, X, X, -, -, -, -, -, -

    b=0;
    log(for(a in [1 to 10]) {b=b+a});
    //logs 55
```

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
