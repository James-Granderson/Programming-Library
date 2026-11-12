# `Memory Bus`

**Concept:** Memory
**Action:** Store
**Object:** `Memory Bus`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** memory-bus, memory, hardware

---

### What It Is

A memory bus is the communication path between a memory controller and memory devices. Depending on the system, the term may describe address, command, and data signaling across a channel; it is not necessarily a single shared wire bundle.

### What It Does

It carries memory commands and data transfers under timing and electrical rules. Channel width, data rate, rank/bank organization, and controller scheduling determine behavior; modern DRAM interfaces use carefully timed parallel signals.

### How to Use

1. Identify the controller, memory channel, and attached devices.
2. Trace command/address and read/write data phases using the applicable protocol.
3. Use platform documentation for supported rates and channel configuration.

### Requirements

A compatible memory controller, memory devices, electrical connection, and protocol timing are required. Details vary by memory generation.

### Representation

```text
CPU ↔ memory controller ═ command/address + data channel ═ DRAM
```
