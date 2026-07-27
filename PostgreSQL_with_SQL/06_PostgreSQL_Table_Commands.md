# PostgreSQL Table Commands

## Introduction

A table is used to store data in PostgreSQL. It consists of **rows (records)** and **columns (fields)**. Before inserting data, a table must be created inside a database. PostgreSQL provides various commands to create, modify, view, and delete tables.

---

# Contents

1. Create Table
2. View Tables
3. Describe Table
4. Rename Table
5. Add Column
6. Drop Column
7. Rename Column
8. Drop Table
9. Useful Table Commands
10. Summary

---

# 1. Create Table

A table is created using the `CREATE TABLE` command.

```sql
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);
```

---

# 2. View Tables

Display all tables in the current database.

```sql
\dt
```

---

# 3. Describe Table

Display the structure of a table including columns, data types, and constraints.

```sql
\d contacts
```

---

# 4. Rename Table

Rename an existing table.

```sql
ALTER TABLE contacts
RENAME TO contact_book;
```

---

# 5. Add Column

Add a new column to an existing table.

```sql
ALTER TABLE contacts
ADD COLUMN address VARCHAR(200);
```

---

# 6. Drop Column

Remove a column from a table.

```sql
ALTER TABLE contacts
DROP COLUMN address;
```

---

# 7. Rename Column

Rename an existing column.

```sql
ALTER TABLE contacts
RENAME COLUMN phone TO mobile;
```

Rename it back if needed.

```sql
ALTER TABLE contacts
RENAME COLUMN mobile TO phone;
```

---

# 8. Drop Table

Delete an entire table from the database.

```sql
DROP TABLE contacts;
```

---

# 9. Useful Table Commands

Show all tables:

```sql
\dt
```

Describe table:

```sql
\d contacts
```

Check current database:

```sql
SELECT current_database();
```

Connect to another database:

```sql
\c student
```

---

# 10. Summary

In this lesson, we learned how to:

- Create a table
- View all tables
- Describe a table structure
- Rename a table
- Add a new column
- Drop a column
- Rename a column
- Delete a table

These commands are the foundation of working with tables in PostgreSQL using the Command Line Interface (CLI).