# update

**Concept:** SQL
**Action:** Update
**Object:** `UPDATE`
**Classification:** Statement
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL statement used to change existing rows in a table.

### What It Does

Sets new column values for rows that match the statement's condition.

### How to Use

Write `UPDATE`, the table name, `SET` with the column assignments, then optionally `WHERE` to limit which rows change.

### Requirements

SQL database  // Provides the table whose rows are modified.
`WHERE`  // Limits the update to specific rows when a condition is needed.

### Representation

```sql
UPDATE users SET age = 31 WHERE name = 'Alice';
```
