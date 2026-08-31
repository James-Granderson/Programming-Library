# global-scope

**Concept:** C
**Action:** Define
**Object:** Global Scope
**Classification:** Scope
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** scope

---

### What It Is

The scope of an identifier declared outside every function and block.

### What It Does

Makes the identifier available from its declaration to the end of the source file, subject to declarations in other scopes that hide it.

### How to Use

Declare a file-scope object before functions that need to use it. Use global scope sparingly because every function in the file can access the object.

### Requirements

C source file  // Contains the file-scope declaration.

### Representation

```c
int total = 0;

int main(void) {
    total = 5;
    return 0;
}
```
