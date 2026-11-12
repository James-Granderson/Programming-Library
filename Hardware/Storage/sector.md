# `Sector`

**Concept:** Storage
**Action:** Persist
**Object:** `Sector`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** sector, storage, hardware

---

### What It Is

A sector is a unit of addressable data on a block storage device. The device's logical sector size may differ from its physical recording unit; common formats include 512-byte logical sectors and 4 KiB sectors.

### What It Does

The storage interface reads or writes sectors as blocks. Filesystems and operating systems combine sectors into larger allocation units; sector addressing does not describe file boundaries.

### How to Use

1. Check the device-reported logical and physical sector sizes.
2. Use aligned block I/O appropriate to the device and filesystem.
3. Distinguish a logical sector from a filesystem block or NAND erase block.

### Requirements

A block device defines sector addressing and a logical sector size. Physical organization and reporting are device-specific.

### Representation

```text
block address N → sector N [logical sector bytes]
```
