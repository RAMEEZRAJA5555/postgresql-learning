# PostgreSQL Data Types

## Introduction

Data types define the kind of data that can be stored in a table column. Choosing the correct data type helps maintain data accuracy, improves performance, and ensures efficient storage.

---

# Contents

1. What are Data Types?
2. Numeric Data Types
3. Character Data Types
4. Boolean Data Type
5. Date and Time Data Types
6. Serial Data Type
7. Commonly Used Data Types
8. Example Table
9. Summary

---

# 1. What are Data Types?

A data type specifies what kind of value a column can store, such as numbers, text, dates, or Boolean values.

Example:

```sql
name VARCHAR(100)
```

This column stores text up to 100 characters.

---

# 2. Numeric Data Types

Used to store numbers.

| Data Type | Description |
|-----------|-------------|
| SMALLINT | Small integer |
| INTEGER | Whole numbers |
| BIGINT | Large whole numbers |
| DECIMAL | Fixed decimal values |
| NUMERIC | Exact numeric values |
| REAL | Single precision decimal |
| DOUBLE PRECISION | Double precision decimal |

Example:

```sql
age INTEGER
salary DECIMAL(10,2)
```

---

# 3. Character Data Types

Used to store text.

| Data Type | Description |
|-----------|-------------|
| CHAR(n) | Fixed-length text |
| VARCHAR(n) | Variable-length text |
| TEXT | Unlimited text |

Example:

```sql
name VARCHAR(100)
address TEXT
```

---

# 4. Boolean Data Type

Stores only two values:

- TRUE
- FALSE

Example:

```sql
is_active BOOLEAN
```

---

# 5. Date and Time Data Types

Used to store dates and times.

| Data Type | Description |
|-----------|-------------|
| DATE | Stores only date |
| TIME | Stores only time |
| TIMESTAMP | Stores date and time |

Example:

```sql
dob DATE
created_at TIMESTAMP
```

---

# 6. Serial Data Type

`SERIAL` automatically generates increasing integer values.

Example:

```sql
contact_id SERIAL PRIMARY KEY
```

Values generated:

```
1
2
3
4
...
```

---

# 7. Commonly Used Data Types

```text
INTEGER      → Whole numbers
VARCHAR      → Text
TEXT         → Long text
BOOLEAN      → True/False
DATE         → Date
TIMESTAMP    → Date and Time
SERIAL       → Auto Increment
DECIMAL      → Decimal Numbers
```

---

# 8. Example Table

```sql
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    age INTEGER,
    is_active BOOLEAN,
    created_at TIMESTAMP
);
```

---

# 9. Summary

In this lesson, we learned:

- What data types are
- Numeric data types
- Character data types
- Boolean data type
- Date and Time data types
- SERIAL data type
- Commonly used PostgreSQL data types

Selecting the correct data type is important for designing efficient and reliable PostgreSQL databases.