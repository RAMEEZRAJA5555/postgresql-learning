# PostgreSQL Constraints

## Introduction

Constraints are rules applied to table columns to ensure that the data stored in the database is accurate, valid, and consistent.

---

# Contents

1. What are Constraints?
2. PRIMARY KEY
3. FOREIGN KEY
4. NOT NULL
5. UNIQUE
6. CHECK
7. DEFAULT
8. Example Table
9. Summary

---

# 1. What are Constraints?

Constraints restrict the type of data that can be stored in a table. They help maintain data integrity and prevent invalid data.

---

# 2. PRIMARY KEY

A PRIMARY KEY uniquely identifies each record in a table.

Properties:

- Unique value
- Cannot be NULL
- Only one PRIMARY KEY per table

Example:

```sql
contact_id SERIAL PRIMARY KEY
```

---

# 3. FOREIGN KEY

A FOREIGN KEY creates a relationship between two tables.

Example:

```sql
CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(contact_id)
);
```

---

# 4. NOT NULL

Ensures a column cannot contain NULL values.

Example:

```sql
name VARCHAR(100) NOT NULL
```

---

# 5. UNIQUE

Ensures duplicate values are not allowed.

Example:

```sql
email VARCHAR(100) UNIQUE
```

---

# 6. CHECK

Validates data based on a condition.

Example:

```sql
age INTEGER CHECK(age >= 18)
```

Only values greater than or equal to 18 are allowed.

---

# 7. DEFAULT

Assigns a default value if none is provided.

Example:

```sql
country VARCHAR(50) DEFAULT 'Pakistan'
```

If no country is entered, PostgreSQL automatically stores **Pakistan**.

---

# 8. Example Table

```sql
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE,
    email VARCHAR(100) UNIQUE,
    age INTEGER CHECK(age >= 18),
    country VARCHAR(50) DEFAULT 'Pakistan'
);
```

---

# 9. Summary

In this lesson, we learned:

- PRIMARY KEY → Uniquely identifies records
- FOREIGN KEY → Creates relationships between tables
- NOT NULL → Prevents NULL values
- UNIQUE → Prevents duplicate values
- CHECK → Validates data using conditions
- DEFAULT → Assigns default values automatically

Constraints help keep PostgreSQL databases accurate, reliable, and consistent.