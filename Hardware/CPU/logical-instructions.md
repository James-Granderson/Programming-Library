# `Logical Instructions`

**Concept:** Cpu
**Action:** Evaluate
**Object:** `Logical Instructions`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** logical-instructions, cpu, hardware

---

### What It Is

Logical instructions perform boolean operations on individual bits of one or more operands, commonly AND, OR, XOR, and NOT. They are distinct from comparisons, although some logical operations may set status flags.

### What It Does

They manipulate bit patterns, often for masks, setting or clearing selected bits, or testing values. The operation is applied across the operand width according to the ISA.

### How to Use

1. Choose an operation and operand width.
2. Apply the boolean truth function to each corresponding bit.
3. Use the result as data or check any documented flag effects.

### Requirements

An ISA implementation with the required logical operations and valid operands is required. Width and flag semantics are architecture-specific.

### Representation

```text
A: 1010
B: 1100
A AND B = 1000
```
