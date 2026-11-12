# `Nvme`

**Concept:** Storage
**Action:** Persist
**Object:** `Nvme`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** nvme, storage, hardware

---

### What It Is

Non-Volatile Memory Express (NVMe) is a command set and host-controller interface designed for nonvolatile storage, commonly used over PCI Express. NVMe is not a storage medium; an NVMe SSD typically uses NAND flash behind its controller.

### What It Does

It defines queues and commands for storage reads, writes, and management, allowing parallel requests with low protocol overhead. Actual speed also depends on the SSD, PCIe link, workload, and thermal limits.

### How to Use

1. Confirm that the host supports NVMe and the device's transport and form factor.
2. Install the device and ensure firmware/OS exposes its NVMe controller and namespace.
3. Use NVMe-aware tools to inspect health, capacity, and link status.

### Requirements

A compatible NVMe host/controller and supported transport (usually PCIe) are required. Device protocol version, lane width, and speed must be supported by the platform.

### Representation

```text
OS driver ⇄ NVMe queues/commands ⇄ controller → flash media
```
