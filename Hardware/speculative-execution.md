# `speculative-execution`

**Concept:** CPU
**Action:** Predict
**Object:** `speculative-execution`
**Classification:** Execution Mechanism
**Environment:** CPU
**Path Type:** N/A
**Tags:** cpu, execution, branch-prediction, pipeline

---

### What It Is

Speculative execution is a CPU technique in which instructions are executed before the processor knows with certainty that they belong to the correct execution path.

### What It Does

Allows the CPU to continue doing useful work while waiting for information needed to determine the actual execution path.

### How to Use

The processor automatically performs speculative execution when supported by its architecture.

### Requirements

CPU architecture supporting speculative execution

### Representation

```text
Branch
  ↓
Predict Path
  ↓
Execute Speculatively
  ↓
Correct? ── Yes → Keep Results
    │
    └──────── No → Discard Speculative Work

