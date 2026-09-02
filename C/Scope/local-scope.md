# `Local Scope`

**Concept:** C
**Action:** Define
**Object:** Local Scope
**Classification:** Scope
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** scope

---

### What It Is

The scope of an identifier declared inside a block, such as a function body.

### What It Does

Makes the identifier available from its declaration to the end of that block only.

### How to Use

Declare a local object inside the smallest block that needs it. The object cannot be referred to outside that block.

### Requirements

C block  // Establishes the local scope.

### Representation

```c
int main(void) {
    int count = 3;
    return count;
}
```
