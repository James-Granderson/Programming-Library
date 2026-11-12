# `Xnor Gate`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Xnor Gate`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** xnor-gate, logic, hardware

---

### What It Is

An XNOR gate is the complement of XOR. For two inputs it outputs 1 when the inputs are equal and 0 when they differ; it is also called an equivalence gate.

### What It Does

It detects matching bit values and is useful in equality checks and parity-related logic. Multi-input forms depend on how the function is defined or cascaded.

### How to Use

1. Compare the input bits.
2. Output 1 when they match and 0 when they differ.
3. For a word comparison, combine bitwise equality results as required.

### Requirements

Compatible binary input levels and an XNOR implementation are required.

### Representation

```text
A B | Y
0 0 | 1
0 1 | 0
1 0 | 0
1 1 | 1
```
