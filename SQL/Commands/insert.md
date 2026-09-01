# `INSERT`

**Concept:** SQL
**Action:** Insert
**Object:** `INSERT`
**Classification:** Statement
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A SQL statement used to add one or more rows to a table.

### What It Does

Creates new rows by writing values into the named columns of a table.

### How to Use

Write `INSERT INTO`, the table name, the column list in parentheses, then `VALUES` and the matching values.

### Requirements

SQL database  // Provides the table that receives the new rows.

### Representation

```sql
INSERT INTO users (name, age) VALUES ('Alice', 30);
```
