# `PRIMARY KEY`

**Concept:** SQL
**Action:** Define
**Object:** `PRIMARY KEY`
**Classification:** Constraint
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A table constraint that marks one column as the unique identifier for each row.

### What It Does

Ensures every row has a distinct, non-null value in the designated column.

### How to Use

Add `PRIMARY KEY` after the column definition inside a `CREATE TABLE` statement.

### Requirements

`CREATE TABLE`  // Provides the table definition that receives the constraint.

### Representation

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```
