# `Memory`

**Concept:** Memory
**Action:** Store
**Object:** `Memory`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** memory, memory, hardware

---

### What It Is

Computer memory is hardware that holds data and instructions for use by a processor or device. The term includes registers, caches, volatile RAM, and nonvolatile memory; it is broader than main memory and distinct from file storage as a system role.

### What It Does

Memory provides addressable state that components read or update. Different technologies trade off latency, capacity, cost, persistence, and location in the hierarchy.

### How to Use

1. Identify the kind of memory and the component that accesses it.
2. Determine whether it is volatile, its address space, and its position in the hierarchy.
3. Trace a read or write through caches and controllers to the relevant device.

### Requirements

A storage technology, access interface, and rules for addressing and data retention are required. Properties depend on the memory class.

### Representation

```text
registers → caches → RAM → persistent storage
 faster/smaller                         larger/slower
```
