# `Power Supply`

**Concept:** Architecture
**Action:** Connect
**Object:** `Power Supply`
**Classification:** Architecture
**Environment:** Computer
**Path Type:** N/A
**Tags:** power-supply, architecture, hardware

---

### What It Is

A computer power supply converts input electrical power into regulated DC output rails for system components. Desktop ATX units and laptop adapters differ in connectors and design, but both must meet the load's voltage and power requirements.

### What It Does

It supplies energy and provides protection and regulation within specified operating limits. The PSU does not determine system performance directly, though inadequate or faulty power can cause instability or shutdowns.

### How to Use

1. Choose a unit with the required form factor, connectors, and adequate rated capacity.
2. Connect board, processor, graphics, and drive power as specified by their manuals.
3. Keep ventilation clear and never open a PSU enclosure; internal capacitors can retain hazardous charge.

### Requirements

A compatible input source, correctly wired connectors, and sufficient capacity on required rails are needed. Ratings and protections vary by model.

### Representation

```text
AC input → conversion/regulation → DC rails → motherboard / CPU / GPU / drives
```
