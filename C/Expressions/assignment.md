# `Assignment Expression`

**Concept:** C
**Action:** Evaluate
**Object:** Assignment Expression
**Classification:** Expression
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** expression

---

### What It Is

An expression that stores a value in an assignable object.

### What It Does

Updates the object on the left side and evaluates to the assigned value.

### How to Use

Place `=`, or a compound assignment operator such as `+=`, between an assignable object and a compatible value.

### Requirements

Assignable object  // Receives the assigned value.

### Representation

```c
int main(void) {
    int count;
    int result = (count = 3);
}
```
