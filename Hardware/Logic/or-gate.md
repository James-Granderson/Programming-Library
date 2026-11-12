# `Or Gate`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Or Gate`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** or-gate, logic, hardware

---

### What It Is

An OR gate produces 1 when at least one of its inputs is 1; it produces 0 only when all inputs are 0.

### What It Does

It combines conditions so that any asserted input can assert the output. The abstract function does not specify electrical behavior or delay.

### How to Use

1. Check whether any input is 1.
2. Set the output to 1 if so; otherwise set it to 0.
3. Check voltage levels and loading in the physical circuit.

### Requirements

Compatible binary input levels and an OR-gate implementation are required.

### Representation

```text
A B | Y
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 1
```
