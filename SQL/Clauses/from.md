# from

**Concept:** SQL
**Action:** Reference
**Object:** `FROM`
**Object Key:** SQL/FROM
**Classification:** Clause
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL clause that denotes the table a query reads from.

### What It Does

Tells the database which table supplies the rows for the query.

### How to Use

Place `FROM` immediately after the column list in a `SELECT`, followed by the table name.

### Requirements

`SELECT`  // Provides the query that `FROM` supplies rows to.

### Representation

```sql
SELECT name FROM users;
```

