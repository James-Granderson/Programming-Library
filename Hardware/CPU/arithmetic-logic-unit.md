# `Arithmetic Logic Unit`

**Concept:** Cpu
**Action:** Evaluate
**Object:** `Arithmetic Logic Unit`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** arithmetic-logic-unit, cpu, hardware

---

### What It Is

An arithmetic logic unit (ALU) is combinational or pipelined CPU circuitry that performs integer arithmetic and bitwise operations. CPUs may have multiple specialized execution units; an ALU is not the whole CPU.

### What It Does

It selects an operation and computes a result from input operands, often producing condition information. The control and scheduling logic decide which operation reaches the unit.

### How to Use

1. Trace the instruction's decoded operation and operand values.
2. Observe the selected ALU function and result path.
3. Check whether flags or exceptions are produced by this operation.

### Requirements

Operand signals, operation control, and circuitry for the required operations are needed. Width and supported functions depend on the design.

### Representation

```text
Operands A,B + operation select → [ ALU ] → result, status
```
