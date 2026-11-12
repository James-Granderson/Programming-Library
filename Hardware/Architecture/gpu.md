# `Gpu`

**Concept:** Architecture
**Action:** Connect
**Object:** `Gpu`
**Classification:** Architecture
**Environment:** Computer
**Path Type:** N/A
**Tags:** gpu, architecture, hardware

---

### What It Is

A graphics processing unit (GPU) is a processor optimized for parallel workloads, especially graphics and image operations. A discrete GPU is a separate device; an integrated GPU shares a processor package and often uses system memory.

### What It Does

A GPU executes graphics or compute workloads through many execution lanes and associated scheduling, memory, and display logic. It complements rather than replaces the CPU, and capabilities vary by architecture and software interface.

### How to Use

1. Provide a workload through a graphics or compute API and select an available GPU device.
2. Transfer or make input data accessible in the GPU's memory domain.
3. Submit work, synchronize when results are needed, and present output through a display engine if applicable.

### Requirements

A compatible GPU, driver/runtime, and supported software API are required. Memory capacity and features vary by device; integrated GPUs may use shared RAM.

### Representation

```text
CPU submits commands → GPU execution units ↔ GPU/system memory → rendered result
```
