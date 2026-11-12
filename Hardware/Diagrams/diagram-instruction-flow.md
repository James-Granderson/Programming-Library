# `Diagram Instruction Flow`

**Concept:** Diagrams
**Action:** Store
**Object:** `Diagram Instruction Flow`
**Classification:** Concept
**Environment:** CPU
**Path Type:** N/A
**Tags:** diagram-instruction-flow, diagrams, hardware

---

### What It Is

An instruction-flow diagram is a visual reference tracing how instructions move through selected CPU stages or queues. It may show sequential execution or overlapping pipeline work; it does not represent a separate hardware device.

### What It Does

It clarifies ordering, stage handoffs, and possible stalls or redirects. The diagram should distinguish program order from simultaneous in-flight work and should not imply that every CPU uses the same stages.

### How to Use

1. Identify whether the view shows one instruction's path or multiple instructions over time.
2. Follow stage labels and arrows, checking how branches, dependencies, or stalls change the path.
3. Use cycle timing or processor documentation for precise latency and issue behavior.

### Requirements

A defined pipeline model, labeled stages, and a legend for direction/time are required. Explain any omitted stages and avoid presenting the view as universal.

### Representation

```text
Program order: I1 → I2 → I3
Pipeline time:  I1: Fetch → Decode → Execute
                I2:        Fetch → Decode → Execute
```
