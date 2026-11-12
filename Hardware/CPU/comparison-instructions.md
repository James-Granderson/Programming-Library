# `Comparison Instructions`

**Concept:** Cpu
**Action:** Execute
**Object:** `Comparison Instructions`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** comparison-instructions, cpu, hardware

---

### What It Is

Comparison instructions test a relation between operands, such as equality or ordering. In some ISAs, a compare is a distinct instruction; in others, a subtract-like operation sets flags and a branch or conditional operation consumes them.

### What It Does

They determine condition information or a boolean result for subsequent control or data operations. Signed and unsigned ordering can differ, so the instruction's defined interpretation matters.

### How to Use

1. Determine the operand width and signed/unsigned interpretation.
2. Evaluate the specified relation or flag effects.
3. Follow the conditional instruction that uses the result, if any.

### Requirements

Supported ISA instructions and valid operands are required. Flag behavior and compare forms are architecture-specific.

### Representation

```text
A,B → compare (equal / less / greater) → condition result or flags
```
