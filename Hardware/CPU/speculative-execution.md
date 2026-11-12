# `Speculative Execution`

**Concept:** Cpu
**Action:** Use
**Object:** `Speculative Execution`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** speculative-execution, cpu, hardware

---

### What It Is

Speculative execution is work performed before the CPU knows whether it will be needed, commonly along a predicted branch path. Results are generally kept provisional until the speculation is validated.

### What It Does

It can hide control or memory latency by doing useful candidate work early. If the prediction is wrong or an exception invalidates the work, the processor discards or rolls back architectural effects; microarchitectural effects may still matter for security analysis.

### How to Use

1. Identify the unresolved condition or predicted path.
2. Track which operations and results are provisional.
3. Follow validation and commit, or the recovery path if speculation fails.

### Requirements

Prediction or another basis for speculation, temporary state, and a recovery mechanism are required. Policies and observable effects vary by design.

### Representation

```text
predict / assume → execute provisionally → validate → commit
                                      └→ discard and recover
```
