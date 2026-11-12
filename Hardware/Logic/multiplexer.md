# `Multiplexer`

**Concept:** Logic
**Action:** Evaluate
**Object:** `Multiplexer`
**Classification:** Logic
**Environment:** Digital Circuit
**Path Type:** N/A
**Tags:** multiplexer, logic, hardware

---

### What It Is

A multiplexer (MUX) is a combinational circuit that selects one of several data inputs and routes it to an output according to select signals.

### What It Does

It lets hardware share a downstream datapath among alternative sources. For 2^n inputs, n select bits can choose an input, subject to the design's encoding and control.

### How to Use

1. Identify data inputs and select-line encoding.
2. Set the select value for the desired source.
3. Trace only the selected input to the output.

### Requirements

Data inputs, select signals, and a MUX implementation with compatible widths are required. Selection timing and behavior during transitions depend on circuit design.

### Representation

```text
D0 ─┐
D1 ─┼─► [MUX] ─► Y
D2 ─┤       ▲
D3 ─┘    select S1,S0
```
