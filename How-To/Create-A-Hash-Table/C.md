# Create A Hash Table

**Concept:** C
**Action:** Create
**Object:** Create A Hash Table
**Classification:** How-To
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** procedure

---

### What It Is

A procedure for creating a fixed-size hash table in C with linear probing.

### What It Does

Stores integer key-value pairs in an array and resolves collisions by checking subsequent array positions.

### How to Use

1. Define an entry with a key, value, and occupancy marker.
2. Choose a table size and hash each key to an initial index.
3. Insert into that index or probe forward until an unoccupied entry is found.
4. Use the same hash-and-probe process to look up a key.

### Requirements

Array  // Stores the table entries.
Hash function  // Maps a key to an initial array index.

### Representation

```c
#include <stdio.h>

#define TABLE_SIZE 5

typedef struct {
    int key;
    int value;
    int occupied;
} Entry;

typedef struct {
    Entry entries[TABLE_SIZE];
} HashTable;

unsigned int hash(int key) {
    return (unsigned int)key % TABLE_SIZE;
}

int insert(HashTable *table, int key, int value) {
    for (unsigned int offset = 0; offset < TABLE_SIZE; offset++) {
        unsigned int index = (hash(key) + offset) % TABLE_SIZE;
        if (!table->entries[index].occupied) {
            table->entries[index] = (Entry){key, value, 1};
            return 1;
        }
    }
    return 0;
}

int main(void) {
    HashTable table = {0};
    insert(&table, 12, 100);
    printf("%d\n", table.entries[hash(12)].value);
    return 0;
}
```
