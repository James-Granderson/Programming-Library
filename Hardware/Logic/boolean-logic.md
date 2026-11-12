# `Boolean Logic`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Boolean Logic`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** boolean-logic, logic, hardware

---

### What It Is

Boolean logic is an algebra over two-valued variables, typically false/true or 0/1, using operations such as AND, OR, and NOT. Digital hardware uses these functions to build combinational and sequential circuits.

### What It Does

Boolean expressions describe how outputs depend on inputs. Simplification can reduce circuit complexity, while state and timing require additional storage elements beyond pure boolean equations.

### How to Use

1. Name the binary inputs and desired output.
2. Write the logical expression or truth table.
3. Implement it with gates and verify every input combination.

### Requirements

A defined boolean interpretation and signals with distinguishable logic levels are required. Real hardware also needs timing and electrical constraints.

### Representation

```text
A B | (A AND B) OR NOT B
0 0 | 1
0 1 | 0
1 0 | 1
1 1 | 1
```
