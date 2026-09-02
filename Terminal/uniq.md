# `uniq`

**Concept:** Shell
**Action:** Filter
**Object:** uniq
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command

---

### What It Is

A shell command that filters adjacent repeated lines from input.
### What It Does

Compares neighboring lines and reports or removes repeated occurrences according to its options.
### How to Use

Run uniq with optional flags and an input file or piped input.
### Requirements

Shell
### Representation
```shell
sort file.txt | uniq
```

### Flags
```text
-c — Prefix each line with its number of occurrences.
-d — Outines that appear more than once.
-u — Output only lines that appear exactly once.
-i — Perform case-insensitive comparisons.
