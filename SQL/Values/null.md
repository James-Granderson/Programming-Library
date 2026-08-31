# null

**Concept:** SQL
**Action:** Represent
**Object:** `NULL`
**Classification:** Null Value
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword, expression

---

### What It Is

A SQL literal that represents the absence of a value in a column.

### What It Does

Marks a column as having no data rather than an empty string or zero.

### How to Use

Write `NULL` as a column value in `INSERT` or `UPDATE`, or compare against it with `IS NULL` or `IS NOT NULL` in a `WHERE` clause.

### Requirements

SQL database  // Interprets `NULL` as missing data in column values.

### Representation

```sql
INSERT INTO users (name, age) VALUES ('Bob', NULL);

SELECT name FROM users WHERE age IS NULL;
```
