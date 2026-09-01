# `Comparison Expression`

**Concept:** C
**Action:** Evaluate
**Object:** Comparison Expression
**Classification:** Expression
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** expression
---

---

### What It Is

An expression that compares two values.

### What It Does

Evaluates to `1` when the comparison is true and `0` when it is false.

### How to Use

Place a comparison operator such as `==`, `!=`, `<`, or `>=` between two comparable values.

### Requirements

Comparable values  // Supply the operands for the comparison.

### Representation

```c
int main(void) {
    int age = 20;
    int is_adult = age >= 18;
}
```
