# printf-format-specifier-catalog

**Concept:** C
**Action:** Reference
**Object:** printf Format Specifier Catalog
**Classification:** Format String
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** format-string

---

### What It Is

A catalog of conversion specifications accepted by the standard C `printf` family.

### What It Does

Shows how a format specification chooses the output representation and the argument type it expects.

### How to Use

Write a conversion specification as:

```text
%[flags][width][.precision][length]conversion
```

Match every conversion specification with an argument of the required type. A mismatched conversion and argument type has undefined behavior.

### Conversion Specifiers

| Conversion | Literal representation | Argument and output |
| --- | --- | --- |
| `d` | `%d` | Signed decimal integer |
| `i` | `%i` | Signed decimal integer |
| `o` | `%o` | Unsigned octal integer |
| `u` | `%u` | Unsigned decimal integer |
| `x` | `%x` | Unsigned hexadecimal integer with lowercase letters |
| `X` | `%X` | Unsigned hexadecimal integer with uppercase letters |
| `b` | `%b` | Unsigned binary integer (C23) |
| `B` | `%B` | Unsigned binary integer with uppercase prefix when supported; optional in C23 |
| `f` | `%f` | Decimal floating-point notation |
| `F` | `%F` | Decimal floating-point notation |
| `e` | `%e` | Scientific floating-point notation with a lowercase exponent |
| `E` | `%E` | Scientific floating-point notation with an uppercase exponent |
| `g` | `%g` | Shorter of decimal or scientific notation with a lowercase exponent |
| `G` | `%G` | Shorter of decimal or scientific notation with an uppercase exponent |
| `a` | `%a` | Hexadecimal floating-point notation with lowercase letters |
| `A` | `%A` | Hexadecimal floating-point notation with uppercase letters |
| `c` | `%c` | Character |
| `s` | `%s` | Character string |
| `p` | `%p` | Pointer value |
| `n` | `%n` | Stores the number of characters written so far through a pointer; it writes no output |
| `%` | `%%` | A literal percent sign; no argument |

### Flags

| Flag | Effect |
| --- | --- |
| `-` | Left-justify in the field |
| `+` | Prefix signed numeric output with a sign |
| space | Prefix a positive signed numeric output with a space when `+` is absent |
| `#` | Use the conversion's alternative form |
| `0` | Pad numeric output with leading zeroes when applicable |

### Width and Precision

| Component | Meaning |
| --- | --- |
| Width | Minimum field width, written as digits or supplied by `*` with an `int` argument |
| Precision | Begins with `.`; its meaning depends on the conversion |
| `.*` | Takes precision from an `int` argument |

For integer conversions, precision sets a minimum digit count. For `f`, `e`, `E`, `a`, and `A`, it controls digits after the radix point. For `g` and `G`, it controls significant digits. For `s`, it limits the bytes written.

### Length Modifiers

| Modifier | Meaning |
| --- | --- |
| `hh`, `h` | Select a narrower integer argument type after default argument promotions |
| `l`, `ll` | Select `long` or `long long` integer forms; `l` also changes `c` and `s` to wide-character forms |
| `j` | Selects an `intmax_t` or `uintmax_t` form |
| `z` | Selects the signed counterpart of `size_t` or the corresponding unsigned form |
| `t` | Selects a `ptrdiff_t` form |
| `L` | Selects `long double` for floating-point conversions |
| `wN`, `wfN` | C23 width modifiers for integer types; support depends on the implementation |

Only specific length-modifier and conversion pairs are valid. Do not combine them freely.

### Requirements

`<stdio.h>`  // Declares `printf`.
Matching argument types  // Each conversion requires the corresponding promoted argument type.

### Representation

```c
#include <stdio.h>

int main(void) {
    int count = 12;
    double ratio = 0.75;
    const char *name = "Ada";

    printf("%-8s count=%04d ratio=%.2f%%\n", name, count, ratio * 100);
    return 0;
}
```
