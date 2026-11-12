# `Pcie`

**Concept:** Architecture
**Action:** Connect
**Object:** `Pcie`
**Classification:** Architecture
**Environment:** Computer
**Path Type:** N/A
**Tags:** pcie, architecture, hardware

---

### What It Is

PCI Express (PCIe) is a high-speed serial interconnect standard used to connect a root complex to endpoints such as graphics, network, and storage devices. Links comprise one or more lanes and are negotiated to a mutually supported generation and width.

### What It Does

PCIe transports packetized transactions over point-to-point links. Switches can fan out connections; a physical slot's size does not guarantee its electrical lane count or generation.

### How to Use

1. Confirm the endpoint, slot or cable, lane wiring, and platform support.
2. Install the device and let firmware/software enumerate the PCIe link.
3. Check negotiated generation and width when diagnosing performance or compatibility.

### Requirements

A compatible root complex, endpoint, physical connection, and available lanes are required. Speed, lane count, power, and features depend on both devices and platform.

### Representation

```text
Root complex ── xN serial lanes ──► PCIe endpoint
                 (optional switch / fan-out)
```
