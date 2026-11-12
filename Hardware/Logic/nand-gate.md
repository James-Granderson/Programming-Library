# `Nand Gate`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Nand Gate`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** nand-gate, logic, hardware

---

### What It Is

A NAND gate produces the inverse of the AND of its inputs: its output is 0 only when all inputs are 1. NAND is a functionally complete gate, meaning other boolean functions can be constructed from NAND gates alone.

### What It Does

It combines inputs and inverts the conjunction. This property is useful in logic design and in transistor-level implementations, but it does not imply every NAND circuit is optimal for every purpose.

### How to Use

1. Evaluate the AND condition across inputs.
2. Invert that result to obtain the NAND output.
3. For a circuit, observe the technology's timing and drive limits.

### Requirements

Compatible binary input levels and a NAND implementation are required.

### Representation

```text
A B | Y
0 0 | 1
0 1 | 1
1 0 | 1
1 1 | 0
```
