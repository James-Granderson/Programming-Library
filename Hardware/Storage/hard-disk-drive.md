# `Hard Disk Drive`

**Concept:** Storage
**Action:** Persist
**Object:** `Hard Disk Drive`
**Classification:** Storage
**Environment:** Computer
**Path Type:** N/A
**Tags:** hard-disk-drive, storage, hardware

---

### What It Is

A hard-disk drive (HDD) stores data magnetically on rotating platters read and written by moving heads. It is a nonvolatile mechanical storage device, distinct from a solid-state drive.

### What It Does

The controller positions a head over tracks and sectors and transfers data as the platter rotates. Seek and rotational delays make random access slower than solid-state access, while HDDs often offer high capacity at low cost.

### How to Use

1. Connect the drive using a supported interface and power connector.
2. Initialize and format it with a filesystem before ordinary file use.
3. Handle it as a mechanical device: avoid shock, monitor health, and keep backups.

### Requirements

A compatible controller/interface, power, mounting, and OS support are required. Capacity, speed, and sector format vary by model.

### Representation

```text
controller → head ⇄ magnetic sectors on rotating platter
```
