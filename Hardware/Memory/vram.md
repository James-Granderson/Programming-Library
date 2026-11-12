# `Vram`

**Concept:** Memory
**Action:** Store
**Object:** `Vram`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** vram, memory, hardware

---

### What It Is

Video RAM (VRAM) is memory available to a graphics processor for resources such as textures, frame buffers, and compute data. Discrete GPUs commonly use dedicated graphics memory; integrated GPUs often use a portion of system RAM instead.

### What It Does

It supplies high-bandwidth data to graphics execution and display hardware. ‘VRAM’ describes a role, not one memory technology; dedicated GPU memory may use specialized DRAM, while exact types vary by product.

### How to Use

1. Check whether the GPU has dedicated memory or uses shared system memory.
2. Monitor capacity and bandwidth needs for the workload.
3. Distinguish graphics memory from a display's own panel buffer, if present.

### Requirements

A GPU or graphics engine and an accessible memory pool are required. Capacity, technology, and sharing depend on the platform.

### Representation

```text
GPU ↔ graphics memory (dedicated)
Integrated GPU ↔ shared system RAM
```
