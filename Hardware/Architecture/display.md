# `Display`

**Concept:** Architecture
**Action:** Connect
**Object:** `Display`
**Classification:** Architecture
**Environment:** Computer
**Path Type:** N/A
**Tags:** display, architecture, hardware

---

### What It Is

A display is an output device that presents images, text, or video. A computer display panel converts an incoming video signal into visible pixels; the GPU or display engine normally generates the signal, while the panel is not itself the graphics processor.

### What It Does

It receives a timed pixel stream or a negotiated digital display link, then drives its pixel elements and manages panel-specific functions. Resolution, refresh rate, color format, and link support constrain what can be shown.

### How to Use

1. Connect the display using a mutually supported interface.
2. Select a supported resolution, refresh rate, and color mode in the system.
3. Distinguish a blank signal or link problem from an application rendering problem.

### Requirements

A display, a compatible video output/link, and appropriate power are needed. Supported modes depend on both source and display.

### Representation

```text
Application → GPU/display engine → video link → Display panel → light
```
