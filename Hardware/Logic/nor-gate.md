# `Nor Gate`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Nor Gate`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** nor-gate, logic, hardware

---

### What It Is

A NOR gate produces the inverse of the OR of its inputs: its output is 1 only when every input is 0. NOR, like NAND, is functionally complete.

### What It Does

It detects whether any input is asserted and inverts the result. Physical behavior includes propagation delay and electrical constraints not shown by the truth table.

### How to Use

1. Evaluate whether any input is 1.
2. Invert the OR result; output 1 only when none are asserted.
3. Check compatible logic levels in a circuit implementation.

### Requirements

Compatible binary input levels and a NOR implementation are required.

### Representation

```text
A B | Y
0 0 | 1
0 1 | 0
1 0 | 0
1 1 | 0
```
