# `Nand Flash`

**Concept:** Storage
**Action:** Persist
**Object:** `Nand Flash`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** nand-flash, storage, hardware

---

### What It Is

NAND flash is a nonvolatile semiconductor memory organized in strings and arrays of cells that store charge states. It is programmed and erased in larger units than it is read; exact cell and block organization depends on the NAND generation.

### What It Does

It retains data without power and is widely used in SSDs, memory cards, and USB drives. NAND has finite program/erase endurance and requires management such as error correction and bad-block handling, usually provided by a controller.

### How to Use

1. Treat NAND as raw media only when working with a controller or flash-aware system.
2. Use an SSD or managed flash device for normal block/file access.
3. Account for endurance, retention, and error correction in device design.

### Requirements

NAND cells, a compatible controller/management layer for practical use, and error handling are needed. Cell type, endurance, and performance vary.

### Representation

```text
host reads/writes → flash controller (ECC, mapping, wear management) → NAND arrays
```
