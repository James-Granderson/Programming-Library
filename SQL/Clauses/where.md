# `WHERE`

**Concept:** SQL
**Action:** Filter
**Object:** `WHERE`
**Classification:** Clause
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL clause used to restrict which rows a statement returns or affects.

### What It Does

Applies a condition so only rows that match the statement are included.

### How to Use

Place `WHERE` after `FROM` in a `SELECT`, or after the target table in an `UPDATE` or `DELETE`, followed by the condition.

### Requirements

`SELECT`  // Provides the statement that `WHERE` filters.

### Representation

```sql
SELECT name FROM users WHERE age > 18;
```

