# create-table

**Concept:** SQL
**Action:** Define
**Object:** `CREATE TABLE`
**Classification:** Statement
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL statement used to create a new table with named columns and types.

### What It Does

Defines a table structure by declaring each column name and its data type.

### How to Use

Write `CREATE TABLE`, the table name, then list each column and its type inside parentheses.

### Requirements

SQL database  // Stores the new table definition.

### Representation

```sql
CREATE TABLE users (
    id INT,
    name VARCHAR(50)
);
```
