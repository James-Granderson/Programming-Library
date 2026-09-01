# `Create A Doubly Linked List`

**Concept:** C
**Action:** Create
**Object:** Create A Doubly Linked List
**Classification:** How-To
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** procedure
---

---

### What It Is

A procedure for creating a doubly linked list in C.

### What It Does

Builds a sequence of nodes in which each node stores a value plus pointers to both its next and previous nodes.

### How to Use

1. Define a node containing a value, a `next` pointer, and a `previous` pointer.
2. Create each node with `malloc` and initialize both links to `NULL`.
3. Set the current tail's `next` pointer to the new node.
4. Set the new node's `previous` pointer to the former tail.
5. Update the tail, traverse in either direction, then free every node.

### Requirements

C language  // Defines structures and pointers.
`stdlib.h`  // Declares `malloc` and `free`.

### Representation

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *previous;
    struct Node *next;
} Node;

Node *create_node(int value) {
    Node *node = malloc(sizeof *node);
    if (node == NULL) {
        return NULL;
    }

    node->value = value;
    node->previous = NULL;
    node->next = NULL;
    return node;
}

int main(void) {
    Node *head = create_node(10);
    Node *second = create_node(20);
    Node *tail = create_node(30);

    if (head == NULL || second == NULL || tail == NULL) {
        free(head);
        free(second);
        free(tail);
        return 1;
    }

    head->next = second;
    second->previous = head;
    second->next = tail;
    tail->previous = second;

    for (Node *current = head; current != NULL; current = current->next) {
        printf("%d\n", current->value);
    }

    for (Node *current = tail; current != NULL; current = current->previous) {
        printf("%d\n", current->value);
    }

    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}
```
