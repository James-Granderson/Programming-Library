# `Storage Controller`

**Concept:** Storage
**Action:** Execute
**Object:** `Storage Controller`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** storage-controller, storage, hardware

---

### What It Is

A storage controller manages communication between a host and one or more storage devices. It may be integrated into a drive, motherboard chipset, host bus adapter, or RAID adapter.

### What It Does

It interprets commands, schedules transfers, and handles device-specific operations; drive controllers also translate logical block addresses to physical media locations. RAID-capable controllers may add redundancy but are not required for ordinary storage.

### How to Use

1. Identify where the controller resides and which interface/protocol it supports.
2. Follow a host read/write command through the controller to the device.
3. Check driver, firmware, queue, and error-reporting behavior when troubleshooting.

### Requirements

A host interface, compatible controller firmware/driver, and supported device protocol are required. Features such as RAID and caching vary by controller.

### Representation

```text
host command → storage controller → device command/media → completion/data
```
