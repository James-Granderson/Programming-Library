# varchar

**Concept:** SQL
**Action:** Declare
**Object:** `VARCHAR`
**Classification:** Data Type
**Environment:** Any SQL database
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A SQL data type used to store text up to a specified maximum length.

### What It Does

Holds character strings whose length does not exceed the declared limit.

### How to Use

Write `VARCHAR` followed by the maximum length in parentheses when defining a column.

### Requirements

SQL database  // Processes column definitions that use `VARCHAR`.

### Representation

```sql
CREATE TABLE users (
    name VARCHAR(50)
);
```
