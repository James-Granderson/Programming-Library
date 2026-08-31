# delete

**Concept:** SQL
**Action:** Delete
**Object:** `DELETE`
**Classification:** Statement
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL statement used to remove rows from a table.

### What It Does

Permanently deletes rows that match the statement's condition.

### How to Use

Write `DELETE FROM`, the table name, then optionally `WHERE` to specify which rows to remove.

### Requirements

SQL database  // Provides the table whose rows are deleted.
`WHERE`  // Limits the delete to specific rows when a condition is needed.

### Representation

```sql
DELETE FROM users WHERE name = 'Alice';
```
