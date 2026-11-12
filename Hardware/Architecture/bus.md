# `Bus`

**Concept:** Architecture
**Action:** Connect
**Object:** `Bus`
**Classification:** Architecture
**Environment:** Computer
**Path Type:** N/A
**Tags:** bus, architecture, hardware

---

### What It Is

A bus is a shared or point-to-point interconnect that carries signals between components. Depending on the design, it may carry data, addresses, control signals, or some combination; modern systems also use switched fabrics and serial links that are not simple shared buses.

### What It Does

The interconnect transports transactions such as reads, writes, or peripheral messages. Protocol rules define arbitration, ordering, timing, and how endpoints indicate a transfer; bandwidth and latency depend on the implementation.

### How to Use

1. Identify the bus protocol and its endpoints.
2. Follow the address/control phase and corresponding data phase where the protocol defines them.
3. Use the platform specification for signal, timing, and throughput limits.

### Requirements

Compatible electrical interfaces and a shared protocol are required. Topology, width, clocking, and arbitration are design-specific.

### Representation

```text
Requester ── address/control + data ──► Interconnect ──► Target
```
