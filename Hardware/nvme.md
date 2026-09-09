
nvme

Concept: Hardware
Action: Communicate
Object: nvme
Classification: Storage Protocol
Environment: Computer
Path Type: N/A
Tags: hardware, storage, ssd, pcie

What It Is

NVMe (Non-Volatile Memory Express) is a storage protocol designed for non-volatile memory devices such asern SSDs.

What It Does

Provides a low-latency, high-parallelism interface for communicating with SSD storage, commonly over PCIe.

How to Use

An NVMe SSD communicates with the computer through an NVMe controller and typically a PCIe connection.

Requirements

NVMe-compatible storage and interface

Representation
CPU / Chipset
      ↓
    PCIe
      ↓
 NVMe Controller
      ↓
   NAND Flash

