# `And Gate`

**Concept:** Logic
**Action:** Evaluate
**Object:** `And Gate`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** and-gate, logic, hardware

---

### What It Is

An AND gate is a digital logic gate whose output is 1 only when every input is 1. It implements conjunction in boolean logic.

### What It Does

The gate combines input voltage levels into a logic output according to the truth function; real circuits have propagation delay and electrical limits.

### How to Use

1. List the inputs as 0 or 1.
2. Set the output to 1 only if all inputs are 1.
3. Check fan-out and voltage compatibility in a physical circuit.

### Requirements

A logic-family implementation, valid supply levels, and defined input signals are required.

### Representation

```text
A B | Y
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1
```
