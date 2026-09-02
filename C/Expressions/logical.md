# `Logical Expression`

**Concept:** C
**Action:** Evaluate
**Object:** Logical Expression
**Classification:** Expression
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** expression

---

### What It Is

An expression that combines or negates truth-like values.

### What It Does

Evaluates to `1` or `0` by using `&&`, `||`, or `!`.

### How to Use

Use `&&` when both conditions must be true, `||` when either condition may or may not be true, and `!` to negate a condition.

### Requirements

Condition expressions  // Supply values interpreted as true or false.

### Representation

```c
int main(void) {
    int age = 20;
    int has_ticket = 1;
    int can_enter = age >= 18 && has_ticket;
}
```

