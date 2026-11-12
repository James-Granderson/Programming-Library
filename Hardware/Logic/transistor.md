# `Transistor`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Transistor`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** transistor, logic, hardware

---

### What It Is

A transistor is a semiconductor device that controls current between terminals using an input voltage or current. CMOS logic commonly pairs n-channel and p-channel MOSFETs; other transistor types serve different roles.

### What It Does

Transistors act as switches or amplifiers and are combined into logic gates, memory cells, and analog circuits. A digital transistor's switching is an electrical process with finite delay and power use.

### How to Use

1. Identify transistor type and terminal roles from the circuit.
2. Trace how the control terminal affects the conduction path.
3. Use device ratings and bias conditions rather than treating it as an ideal switch.

### Requirements

A suitable device, bias or gate drive, and circuit within voltage/current/thermal ratings are required.

### Representation

```text
control input → transistor changes conduction → output node pulled high/low
```
