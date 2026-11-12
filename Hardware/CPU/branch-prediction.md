# `Branch Prediction`

**Concept:** Cpu
**Action:** Execute
**Object:** `Branch Prediction`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** branch-prediction, cpu, hardware

---

### What It Is

Branch prediction is a CPU technique that estimates the direction and/or target of a control-flow branch before its condition is resolved. Predictors use history and may be static, dynamic, or combined.

### What It Does

A prediction lets the front end fetch likely-next instructions without waiting for the branch result. A correct prediction avoids some control-flow delay; a wrong one requires discarding affected work and redirecting fetch. Prediction is not the same as executing the branch speculatively.

### How to Use

1. Identify the conditional or indirect branch in the instruction stream.
2. Compare predicted next address with the resolved direction and target.
3. Interpret a misprediction as a redirect cost, not a change to architectural results.

### Requirements

A processor front end with prediction state and branch-resolution logic is required. Predictor design and penalty are implementation-specific.

### Representation

```text
branch encountered → predictor chooses next path → branch resolves → correct: continue / wrong: redirect
```
