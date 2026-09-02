# `Function Call Expression`

**Concept:** C
**Action:** Evaluate
**Object:** Function Call Expression
**Classification:** Expression
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** expression

---

### What It Is

An expression that invokes a function.

### What It Does

Passes argument values to a function and evaluates to its returned value when the function has one.

### How to Use

Write a function name followed by parentheses containing any required arguments.

### Requirements

Function declaration  // Specifies the function and its parameters.

### Representation

```c
int square(int number) {
    return number * number;
}

int main(void) {
    int value = square(4);
}
```
