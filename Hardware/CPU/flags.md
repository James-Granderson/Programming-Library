# `Flags`

**Concept:** Cpu
**Action:** Use
**Object:** `Flags`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** flags, cpu, hardware

---

### What It Is

CPU flags are architecturally visible or internal status bits that record conditions such as zero, carry, sign, or overflow. Which flags exist and which instructions update them depends on the ISA.

### What It Does

A later conditional branch or instruction can test selected flags to choose an action. Flags are not a general-purpose register and are not universally produced by every arithmetic operation.

### How to Use

1. Check the ISA rule for which operation sets or preserves each flag.
2. Evaluate the relevant status bit after the operation.
3. Trace how a conditional instruction consumes that flag.

### Requirements

A processor and instruction set with the relevant status state and flag-consuming operations are required. Flag meanings are architecture-specific.

### Representation

```text
operation → status bits (Z, C, N, V, as defined) → conditional use
```
