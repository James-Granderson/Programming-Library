# `ORDER BY`

**Concept:** SQL
**Action:** Sort
**Object:** `ORDER BY`
**Classification:** Clause
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL clause used to sort the rows returned by a query.

### What It Does

Orders the result set by one or more columns, ascending or descending.

### How to Use

Place `ORDER BY` at the end of a `SELECT`, name the column to sort by, and add `ASC` or `DESC` when the sort direction matters.

### Requirements

`SELECT`  // Provides the result set that `ORDER BY` sorts.

### Representation

```sql
SELECT name, age FROM users ORDER BY age DESC;
```

