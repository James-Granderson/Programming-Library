# `String`
**Concept:** C
**Action:** Represent
**Object:** String
**Classification:** Array
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** array

---

### What It Is

A sequence of characters stored in an array and terminated by a null character (`'\0'`).

C does not have a built-in `string` data type. A C string is represented using a `char` array.

### What It Does

Stores text as individual characters in consecutive positions in memory.

The `'\0'` at the end tells C where the string ends.

### How to Use

Create a `char` array and initialize it with characters or a string literal.

### Requirements

`char`  // Stores each character.

`'\0'`  // Marks the end of the string.

### Representation

```c
char name[] = "James";
```

In memory, this is essentially:

```text
name
 ↓
┌─────┬─────┬─────┬─────┬─────┬─────┐
│  J  │  a  │  m  │  e  │  s  │ \0  │
└─────┴─────┴─────┴─────┴─────┴─────┘
   0     1     2     3     4     5
```

The characters are stored in the array one after another, and `'\0'` marks the end.

### Notes

A C string is fundamentally:

```text
array of char
      +
   '\0'
```

The `'\0'` is part of the stored array, but it is **not part of the text itself**. It is the marker that tells string functions where the text ends.
