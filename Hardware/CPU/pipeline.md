# `Pipeline`

**Concept:** Cpu
**Action:** Execute
**Object:** `Pipeline`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** pipeline, cpu, hardware

---

### What It Is

A pipeline is a general design pattern that divides work into stages connected by intermediate state. In computer hardware it may refer to an instruction pipeline, a graphics pipeline, or another staged datapath; the context must identify which one.

### What It Does

Each stage transforms or forwards work to the next, allowing different items to be processed concurrently. Throughput may improve after the pipeline fills, while stage imbalance, dependencies, and stalls limit progress.

### How to Use

1. Identify the pipeline's input, stages, and output.
2. Follow one item through the stages and then compare multiple overlapping items.
3. Locate stalls, stage bottlenecks, and the specific pipeline type being described.

### Requirements

Defined stage behavior, inter-stage storage, and control for flow or stalls are required. Stage count and timing depend on the design.

### Representation

```text
Input → [Stage 1] → [Stage 2] → [Stage 3] → Output
             item A →    item B →
```
