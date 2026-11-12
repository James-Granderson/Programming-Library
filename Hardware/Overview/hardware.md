# `Hardware`

**Concept:** Overview
**Action:** Use
**Object:** `Hardware`
**Classification:** Concept
**Environment:** Computer
**Path Type:** N/A
**Tags:** hardware, overview, hardware

---

### What It Is

Computer hardware is the physical equipment and electronic circuitry that computes, stores, communicates, and presents information. It includes processors, memory, storage, interconnects, power and cooling systems, and input/output devices.

### What It Does

Hardware implements operations through physical components and interfaces, following specifications that software and firmware use. Components have different roles: RAM is working memory, storage preserves data, and the CPU executes instructions; no single part represents the whole computer.

### How to Use

1. Start with the system-level component map, then identify the relevant subsystem.
2. Trace data, control, and power through the interfaces connecting components.
3. Consult component specifications for electrical, timing, compatibility, and performance details.

### Requirements

A hardware system needs compatible components, interconnects, power, and appropriate firmware/software to operate. Exact organization differs across computers and embedded systems.

### Representation

```text
Input/output ↔ system interconnect ↔ CPU ↔ memory
                               ↕
                      storage / GPU / devices
```
