# Create A Linked List

**Concept:** C
**Action:** Create
**Object:** Create A Linked List
**Classification:** How-To
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** procedure

---

### What It Is

A procedure for creating a singly linked list in C.

### What It Does

Builds a sequence of nodes in which each node stores a value and a pointer to the next node.

### How to Use

1. Define a node containing a value and a `next` pointer.
2. Create each node with `malloc` and initialize its fields.
3. Link the current tail's `next` pointer to the new node.
4. Move the tail to the new node.
5. Traverse from `head` through `next` to use the list, then free every node.

### Requirements

C language  // Defines structures and pointers.
`stdlib.h`  // Declares `malloc` and `free`.

### Representation

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

Node *create_node(int value) {
    Node *node = malloc(sizeof *node);
    if (node == NULL) {
        return NULL;
    }

    node->value = value;
    node->next = NULL;
    return node;
}

int main(void) {
    Node *head = create_node(10);
    Node *second = create_node(20);
    Node *third = create_node(30);

    if (head == NULL || second == NULL || third == NULL) {
        free(head);
        free(second);
        free(third);
        return 1;
    }

    head->next = second;
    second->next = third;

    for (Node *current = head; current != NULL; current = current->next) {
        printf("%d\n", current->value);
    }

    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}
```
