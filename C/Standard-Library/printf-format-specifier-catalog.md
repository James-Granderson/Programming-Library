# `printf Format Specifier Catalog`

**Concept:** C
**Action:** Reference
**Object:** printf Format Specifier Catalog
**Classification:** Format String
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** format-string
---

---

### What It Is

A reference for the conversion specifiers used by `printf`.

### Representation


| Specifier | Expects            | Displays                                    |
| --------- | ------------------ | ------------------------------------------- |
| `%d`      | signed integer     | decimal integer                             |
| `%i`      | signed integer     | decimal integer                             |
| `%o`      | unsigned integer   | octal integer                               |
| `%u`      | unsigned integer   | decimal integer                             |
| `%x`      | unsigned integer   | hexadecimal, lowercase                      |
| `%X`      | unsigned integer   | hexadecimal, uppercase                      |
| `%f`      | `double`           | decimal floating point                      |
| `%e`      | `double`           | scientific notation, lowercase              |
| `%E`      | `double`           | scientific notation, uppercase              |
| `%g`      | `double`           | shorter decimal/scientific form             |
| `%G`      | `double`           | shorter decimal/scientific form             |
| `%a`      | `double`           | hexadecimal floating point                  |
| `%A`      | `double`           | hexadecimal floating point                  |
| `%c`      | `int`              | character                                   |
| `%s`      | pointer to `char`  | string                                      |
| `%p`      | pointer            | pointer representation                      |
| `%n`      | pointer to integer | stores characters written; displays nothing |
| `%%`      | nothing            | `%`                                         |




### Flags


| Flag | Meaning                             |
| ---- | ----------------------------------- |
| `-`  | left-align                          |
| `+`  | show the sign                       |
|      | space before positive signed output |
| `#`  | alternative form                    |
| `0`  | pad with zeroes                     |




### Width

Sets the minimum number of characters used for the output.

```c
printf("%8d", 42);

```

The output is at least 8 characters wide.

`*` can be used to take the width from an `int` argument.

### Precision

Controls the amount of output produced, depending on the conversion.

```c
printf("%.2f", 3.14159);

```

Produces:

```text
3.14

```



### Length Modifiers

Change the type or interpretation expected by a conversion.

Common modifiers:

```text
hh
h
l
ll
j
z
t
L

```

For example:

```c
printf("%ld", number);

```

uses `l` to specify a `long` integer.

### Format Structure

A format specification can combine these parts:

```text
%[flags][width][.precision][length]conversion

```

For example:

```c
printf("%-8.2f", value);

```

means:

```text
%    start
-    left-align
8    minimum width
.2   precision
f    floating-point output

```



### Requirements

`<stdio.h>` // Declares `printf`.

Matching argument type // Provides the value expected by the conversion specifier.
