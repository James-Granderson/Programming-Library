# `Arithmetic Instructions`

**Concept:** Cpu
**Action:** Execute
**Object:** `Arithmetic Instructions`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** arithmetic-instructions, cpu, hardware

---

### What It Is

Arithmetic instructions are ISA-defined operations that add, subtract, multiply, divide, or otherwise compute numeric results. Their exact forms include operand widths, signedness, and immediate or register operands specified by the instruction set.

### What It Does

The CPU obtains operands, computes a result in an execution unit, and writes or forwards it to a destination. Some operations also update condition flags; latency and throughput vary by processor.

### How to Use

1. Read the instruction-set definition for operands and result width.
2. Identify source values and destination, including any implicit operands.
3. Use the documented flags and overflow behavior when reasoning about the result.

### Requirements

A processor implementing the relevant ISA extension and valid operands are required. Arithmetic semantics, exceptions, and flags are ISA-specific.

### Representation

```text
source operands → arithmetic unit → result / optional status flags
```
