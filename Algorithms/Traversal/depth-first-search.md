# `Depth-First Search`

**Concept:** Algorithms
**Action:** Traverse
**Object:** Depth-First Search
**Classification:** Algorithm
**Environment:** Language-independent
**Path Type:** N/A
**Tags:** algorithm
---

---

### What It Is

A graph or tree traversal algorithm that explores one path as far as possible before backtracking.

### What It Does

Visits every reachable node from a starting node while recording which nodes have already been visited.

### How to Use

Mark the starting node as visited, visit one unvisited neighbor, and repeat recursively or with an explicit stack. Backtrack when a node has no unvisited neighbors.

### Requirements

Graph or tree  // Provides nodes and connections to traverse.
Visited record  // Prevents revisiting nodes in graphs with cycles.

### Representation

```text
visit(node)
for each unvisited neighbor:
    depth-first search(neighbor)
```
