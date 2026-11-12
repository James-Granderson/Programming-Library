# `Adder`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Adder`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** adder, logic, hardware

---

### What It Is

An adder is a combinational circuit that computes the sum of binary operands. A half adder combines two bits; a full adder also accepts a carry-in and produces a carry-out.

### What It Does

It forms the arithmetic datapath used in processors, address generation, and other digital circuits. Multi-bit adders connect bit positions so carries propagate or are computed with faster structures.

### How to Use

1. Provide operand bits and, for a full adder, carry-in.
2. Compute sum and carry for each bit position.
3. Interpret overflow according to the chosen signed or unsigned representation.

### Requirements

Binary input signals and logic for sum/carry are required. Width, carry strategy, and overflow handling depend on the design.

### Representation

```text
A B Cin | Sum Cout
0 0  0  |  0   0
0 1  0  |  1   0
1 1  0  |  0   1
```
