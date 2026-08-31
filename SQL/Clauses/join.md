# join

**Concept:** SQL
**Action:** Combine
**Object:** `JOIN`
**Classification:** Clause
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL clause used to combine rows from two tables based on a related column.

### What It Does

Matches rows across tables and returns the combined result as one result set.

### How to Use

Write `JOIN` after the first table in `FROM`, name the second table, then `ON` with the condition that links the two tables.

### Requirements

`SELECT`  // Provides the query that returns the joined result.
`FROM`  // Provides the first table the join starts from.

### Representation

```sql
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id;
```
