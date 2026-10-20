---
title: "Script Examples"
source: https://automagic4android.com/automagic/1.38/onlinehelp/en/script_examples.html
archived: 2019-05-17
archive_url: https://web.archive.org/web/20190517133649/https://automagic4android.com/automagic/1.38/onlinehelp/en/script_examples.html
category: reference
---

# Script Examples

This page shows some short examples of the most important functions provided by the built-in scripting language.

Copy/Paste the examples into an action **Script** and use **Menu->Execute** to test the action. The output will be written to the Automagic Log accessible with **Menu->Log**.

## String operations

## Test if a variable contains a value (exactly)

value = "test";
result = value == "test";
log(result); // true
result = value == "abcd";
log(result); // false
// using the result in an if-then-else
if (result)
{
log("equal values");
}
else
{
log("different values");
}
// without assigning to a variable first
if (value == "test")
{
log("it's test");
}
else
{
log("value contains something else");
}

## Test if a variable partly contains a specific text

value = "this is a test value";
result = contains(value, "test");
log(result);// true
result = contains(value, "1234");
log(result);// false

## Test if a string matches a regular expression (see [Regular expressions](regular-expressions.md))

value = "my suitcase code is 1234";
result = matches(value, '.\*\\d{4}.\*');
log(result);// true
result = matches(value, '.\*\\d{5}.\*');
log(result);// false

## Find the content of the groups in a regular expression

value = "my code is 1234";
list = newList();
result = matches(value, '.\*(\\d{4}).\*', list);
log(result);// true
log(list);// [my code is 1234, 1234]

## Create a list of lines from a multiline text

value = "line1\nline2\nline3\nline4";
lines = split(value, "\\n"); // or "\\r?\\n" for Windows+Unix
// log each line
for (line in lines)
{
log(line);
}

## Create a list of words

value = "The code of my suitcase is 1234";
words = split(value, "\\W");
log(words);// [The, code, of, my, suitcase, is, 1234]

## Extract the contents of an HTML element

text = "<html>this is the content</html>";
start = indexOf(text, "<html>") + 6;
end = indexOf(text, "</html>", start);
value = substring(text, start, end);
log(value);// this is the content

## Modify a phone number from 00411234567 to 0 0 4 1 1 2 3 4 5 6 7 for better text to speech output

value = "00411234567";
optimized\_value = replaceAll(value, "(.)", "$1 ");
log(optimized\_value);// 0 0 4 1 1 2 3 4 5 6 7

## Test if a file name ends with the suffix .mp3

filename = "test.mp3";
result = endsWith(filename, ".mp3");
log(result);// true

## Strip off the file extension

filename = "test.mp3";
name = left(filename, length(filename) - 4);
log(name);// test

## Convert a text to upper case

value = "This is a test";
upper = toUpperCase(value);
log(upper);// THIS IS A TEST

## Remove whitespace around a text

value = " test ";
trimmed = trim(value);
log(trimmed);// test

## Replace variables in a string literal

date = getDate();// gets the current date+time
number = 42;
value = "Today is the {date,dateformat,dd.MM.yyyy} and the answer to the ultimate question of life, the universe, and everything is {number}";
log(value); // Today is the 29.03.2014 and the answer to the ultimate question of life, the universe, and everything is 42

## Date & Time

## Get and format the current date + time (see [Date Format Pattern](date-format-patterns.md))

date = getDate();
log("It's {date,dateformat,yyyy.MM.dd HH:mm:ss.SSS}");// It's 2014.03.29 14:03:25.437
log("It's {date,dateformat,yyyy.MM.dd hh:mm:ss a}");// It's 2014.03.29 02:03:25 PM
log("It's {date,dateformat,dd. MMM yy}");// It's 29. Mar 14
log("It's {date,dateformat,dd. MMMM yy}");// It's 29. March 14
log("It's {date,dateformat,EEE dd. MMMM yy}");// It's Sat 29. March 14
log("It's {date,dateformat,EEEE dd. MMMM yy}");// It's Saturday 29. March 14
log("It's week {date,dateformat,w}");// It's week 13

## Create a specific date

date = getDate(2014, 3, 29);// 29.03.2014 00:00:00
date = getDate(2014, 3, 29, 14, 3, 0);// 29.03.2014 14:03:00
date = getDate(date, 13, 0, 0);// 29.03.2014 13:00:00

## Duration between two dates

date1 = getDate(2014, 3, 29, 14, 0, 0);// 29.03.2014 14:00:00
date2 = getDate(2014, 3, 29, 15, 7, 30);// 29.03.2014 15:07:30
difference = date2 - date1;
// log difference in milliseconds
log(difference);// 4050000
// log difference in seconds
log(difference/1000);// 4050
// log difference in duration format
log(getDurationString(difference));// 1h 7m 30s
// log difference in format HH:mm:ss (only works when less than 24 hours)
log("{difference,dateformat,timezone,UTC,HH:mm:ss}");// 01:07:30

## Get the date from a text value and reformat

value = "03/29/2014 14:00";
date = getDate(value, "MM/dd/yyyy HH:mm");
log("{date,dateformat,EEEE dd. MMMM}");// Saturday 29. March

## Modifying a date

date = getDate(2014, 3, 29, 14, 0, 0);// 29.03.2014 14:00:00
new\_date = addSeconds(date, 30);// 29.03.2014 14:00:30
new\_date = addMinutes(date, 15);// 29.03.2014 14:15:00
new\_date = addHours(date, 3);// 29.03.2014 17:00:00
// the same by adding milliseconds
new\_date = date + 30\*1000;// 29.03.2014 14:00:30
new\_date = date + 15\*60\*1000;// 29.03.2014 14:15:00
new\_date = date + 3\*60\*60\*1000;// 29.03.2014 17:00:00

## Lists

## Creating lists

list = newList();
log(list);// [] (empty)
list = newList("a", "b", "c");
log(list);// [a, b, c]
list = [1 to 10];
log(list);// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Adding elements to a list

list = newList();
// adding elements
addElement(list, "a");
addElement(list, "b");
addElement(list, "c");
addElement(list, "d");
addElement(list, "e");
log(list);// [a, b, c, d, e]

## Sorting the values in a list

list = newList("c", "a", "d", "b");
sort(list);
log(list);// [a, b, c, d]

## Reversing the values in a list

list = newList("a", "b", "c", "d");
reverse(list);
log(list);// [d, c, b, a]

## Finding the index of an element

list = newList("a", "b", "c", "d");
index = indexOfElement(list, "c");
log(index);// 2

## Remove an element at a specific index

list = newList("a", "b", "c", "d");
removeElement(list, 2);
log(list);// [a, b, d]

## Inserting an element into the list

list = newList("a", "b", "c", "d");
addElement(list, 2, "x");
log(list);// [a, b, x, c, d]

## Test if an element is in the list

list = newList("a", "b", "c", "d");
result = containsElement(list, "c");
log(result);// true

## Adding an element if it is not in the list yet

list = newList("a", "b", "c", "d");
element = "x";
if (not containsElement(list, element))
{
addElement(list, element);
}
log(list);// [a, b, c, d, x]

## Removing value "c" from the list

list = newList("a", "b", "c", "d");
removeElementValue(list, "c");
log(list);// [a, b, d]

## Testing the number of elements in a list

list = newList("a", "b", "c", "d");
length = length(list);
log(length);// 4

## Adding an element to the list but keeping the list 4 element long

list = newList("a", "b", "c", "d");
addElement(list, "x");
if (length(list) > 4)
{
removeElement(list, 0);
}
log(list);// [b, c, d, x]

## Looping over the elements of a list

list = newList("a", "b", "c", "d");
for (element in list)
{
log(element);
}
// logs a, b, c, d each on a separate line

## Maps

## Creating an empty map

map = newMap();
log(map);// {} (empty)

## Adding key/value-pairs to a map

map = newMap();
addMapEntry(map, "key1", "a");
addMapEntry(map, "key2", "b");
addMapEntry(map, "key3", "c");
log(map);// {key1=a, key2=b, key3=c}

## overwriting an entry

map = newMap();
addMapEntry(map, "key1", "a");
addMapEntry(map, "key2", "b");
addMapEntry(map, "key3", "c");
addMapEntry(map, "key3", "x");
log(map);// {key1=a, key3=b, key3=x}

## Accessing the value for a key

map = newMap();
addMapEntry(map, "key1", "a");
addMapEntry(map, "key2", "b");
addMapEntry(map, "key3", "c");
value = getMapValue(map, "key2");
log(value);// b

## get a list of all keys and values in map

map = newMap();
addMapEntry(map, "key1", "a");
addMapEntry(map, "key2", "b");
addMapEntry(map, "key3", "c");
// get a list of all values in map
values = getMapValues(map);
log(values);// [a, b, c]
// get a list of all keys in map
values = getMapKeys(map);
log(values);// [key1, key2, key3]

## XML

The examples in this section use the following input XML (in variable `input`):
```
<books>
    <book>
        <title>Book 1</title>
        <price>12.50</price>
        <pages format="A4">745</pages>
    </book>
    <book>
        <title>Book 2</title>
        <price>35.70</price>
        <pages format="A5">120</pages>
    </book>
    <book>
        <title>Book 3</title>
        <price>17.90</price>
        <pages format="letter">1230</pages>
    </book>
</books>
```

## Extract book titles

// title of the first book
title = evaluateXPathAsString(input, "/books/book[1]/title");
log(title);// Book 1
// title of the second book
title = evaluateXPathAsString(input, "/books/book[2]/title");
log(title);// Book 2
// title of the last book
title = evaluateXPathAsString(input, "/books/book[last()]/title");
log(title);// Book 3

## Extract the price of the books

// price of the book with title 'Book 1'
price = evaluateXPathAsString(input, "/books/book[title='Book 1']/price");
log(price);// 12.50
// price of the first book with more than 1000 pages
price = evaluateXPathAsString(input, "/books/book[pages>1000]/price");
log(price);// 17.90

## Print the format of Book 1

format = evaluateXPathAsString(input, "/books/book[title='Book 1']/pages/@format");
log(format);// A4

## Print Book title of book with page format A5

format = evaluateXPathAsString(input, "/books/book/pages[@format='A5']/../title");
log(format);// Book 2

## Number theory

## RSA (uses experimental functions)

p = randomProbablePrime(512);
q = randomProbablePrime(512);
phi = (p-1)\*(q-1);
n = p\*q;
e = 65537;
pk = modInverse(e, phi);
log("n: " + n);
orig = "This is a test";
log("orig: " + orig);
m = convertStringToBigInteger(orig);
log("m: " + m);
enc = modPow(m, e, n);
log("encoded: " + enc);
dec = modPow(enc, pk, n);
log("decoded: " + convertBigIntegerToString(dec));

## Diffie Hellman (uses experimental functions)

g = 5;
p = randomProbablePrime(512);
a = 6;
b = 15;
alice = modPow(g, a, p);
bob = modPow(g, b, p);
log(s = modPow(bob, a, p));
log(s = modPow(alice, b, p));

---

[← Indeks referensi](README.md) · [Peta dokumentasi](../README.md)
