# `Storage`

**Concept:** Storage
**Action:** Persist
**Object:** `Storage`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** storage, storage, hardware

---

### What It Is

Computer storage is hardware or a service that retains data, commonly after power is removed. Persistent storage includes SSDs, HDDs, and other media; it is distinct from volatile working memory such as RAM.

### What It Does

Storage preserves files, programs, and other data and supplies them through device, filesystem, or network interfaces. Capacity, latency, throughput, durability, and access method vary widely.

### How to Use

1. Choose storage based on persistence, capacity, performance, and interface needs.
2. Use a filesystem or block interface to organize and access data.
3. Protect important data with backups and verify durability requirements.

### Requirements

A storage medium or service, compatible controller/interface, and software support are needed. Persistence and reliability depend on the technology and configuration.

### Representation

```text
application → filesystem/block layer → controller/interface → persistent storage
```
