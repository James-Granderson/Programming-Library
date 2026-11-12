# `Sata`

**Concept:** Storage
**Action:** Persist
**Object:** `Sata`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** sata, storage, hardware

---

### What It Is

Serial ATA (SATA) is a serial interface standard commonly used to connect storage devices such as HDDs and SATA SSDs to a host controller. SATA specifies link communication; it is not the storage medium itself.

### What It Does

It transports commands and data between the host and a device. SATA devices commonly use the ATA command set, often through AHCI, while interface generation, negotiated speed, and device limits constrain throughput.

### How to Use

1. Connect a SATA data cable to the host and appropriate power to the drive.
2. Check controller mode and device detection in firmware and the operating system.
3. Verify negotiated link speed when diagnosing bottlenecks.

### Requirements

A compatible SATA host port/controller, device, data cable, and power are required. Supported rates depend on both ends and the link.

### Representation

```text
OS/storage driver → SATA host ⇄ serial link ⇄ SATA drive
```
