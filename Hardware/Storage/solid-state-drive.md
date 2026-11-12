# `Solid State Drive`

**Concept:** Storage
**Action:** Persist
**Object:** `Solid State Drive`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** solid-state-drive, storage, hardware

---

### What It Is

A solid-state drive (SSD) is a nonvolatile storage device built from semiconductor memory, commonly NAND flash, with a controller that presents a block-device interface. Unlike an HDD, it has no spinning platters or moving read/write heads.

### What It Does

The controller maps logical block requests to flash, performs error correction and wear management, and may use caching. Random access is typically much faster than on an HDD, but performance and endurance vary by device and workload.

### How to Use

1. Check interface, form factor, capacity, and OS compatibility.
2. Install and initialize the drive, then format it if it will hold files.
3. Monitor health and maintain backups; avoid assuming all SSDs have the same endurance or sustained speed.

### Requirements

A compatible host interface, SSD controller, power, and OS driver support are required. NAND type, cache, performance, and endurance are model-specific.

### Representation

```text
host block request → SSD controller → NAND flash (mapping / ECC / wear management)
```
