# `Conditional Expression`

**Concept:** C
**Action:** Evaluate
**Object:** Conditional Expression
**Classification:** Expression
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** expression

---

### What It Is

An expression that selects one of two values from a condition.

### What It Does

Evaluates the expression after `?` when the condition is true; otherwise it evaluates the expression after `:`.

### How to Use

Write a condition, then `?`, the value to use when true, `:`, and the value to use when false.

### Requirements

Condition expression  // Determines which result is selected.

### Representation

```c
int main(void) {
    int left = 8;
    int right = 5;
    int larger = left > right ? left : right;
}
```
