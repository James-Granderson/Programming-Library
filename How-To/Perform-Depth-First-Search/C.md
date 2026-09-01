# `Perform Depth-First Search`

**Concept:** C
**Action:** Traverse
**Object:** Perform Depth-First Search
**Classification:** How-To
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** procedure
---

---

### What It Is

A procedure for traversing a graph with depth-first search in C.

### What It Does

Visits a starting vertex, then recursively visits each unvisited neighbor before backtracking.

### How to Use

1. Represent the graph as an adjacency matrix.
2. Create an array that records which vertices were visited.
3. Mark the current vertex as visited.
4. Recursively visit each adjacent vertex that has not yet been visited.

### Requirements

Array  // Represents the graph and the visited record.
Function Call Expression  // Recursively visits each neighbor.

### Representation

```c
#include <stdio.h>

#define VERTICES 5

void depth_first_search(int graph[VERTICES][VERTICES], int visited[VERTICES], int vertex) {
    visited[vertex] = 1;
    printf("%d ", vertex);

    for (int neighbor = 0; neighbor < VERTICES; neighbor++) {
        if (graph[vertex][neighbor] && !visited[neighbor]) {
            depth_first_search(graph, visited, neighbor);
        }
    }
}

int main(void) {
    int graph[VERTICES][VERTICES] = {
        {0, 1, 1, 0, 0},
        {1, 0, 0, 1, 0},
        {1, 0, 0, 0, 1},
        {0, 1, 0, 0, 0},
        {0, 0, 1, 0, 0}
    };
    int visited[VERTICES] = {0};

    depth_first_search(graph, visited, 0);
    printf("\n");
    return 0;
}
```
