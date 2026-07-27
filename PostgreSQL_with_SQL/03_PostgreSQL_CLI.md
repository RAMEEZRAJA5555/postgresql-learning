# PostgreSQL Command-Line Interface (CLI)

## What is psql?

`psql` is the official Command-Line Interface (CLI) for PostgreSQL. It allows users to connect to a PostgreSQL server and execute SQL commands.

Before connecting, check whether the PostgreSQL server is running:

```bash
pg_isready
```

If the output is:

```text
localhost:5432 - accepting connections
```

then the PostgreSQL server is running and ready to accept connections.

---

## Connect to PostgreSQL

Connect as the default superuser:

```bash
psql -U postgres
```

Connect to a specific database:

```bash
psql -U postgres -d mydb -h localhost -p 5432
```

### Command Options

| Option | Description |
|---------|-------------|
| `psql` | Starts the PostgreSQL CLI |
| `-U` | Specifies the username |
| `postgres` | Default PostgreSQL superuser |
| `-d mydb` | Connects to the `mydb` database |
| `-h localhost` | Connects to the local PostgreSQL server |
| `-p 5432` | Uses the default PostgreSQL port |

---

## Common psql Commands

| Command | Description |
|---------|-------------|
| `\l` | List all databases |
| `\c mydb` | Connect to the `mydb` database |
| `\dt` | List all tables in the current database |
| `\d users` | Describe the `users` table |
| `\du` | List all users (roles) |
| `\q` | Quit psql |
| `\?` | Show help for psql commands |
| `\h SELECT` | Show help for the SQL `SELECT` command |

---

## psql Commands vs SQL Commands

**psql Commands (Meta Commands)**

These commands begin with a backslash (`\`) and are executed by the `psql` program.

Examples:

```text
\l
\c
\dt
\d
\du
\q
```

**SQL Commands**

These are standard SQL statements executed by the PostgreSQL server.

Examples:

```sql
CREATE DATABASE bookstore;

CREATE TABLE books (...);

INSERT INTO books VALUES (...);

SELECT * FROM books;
```

---

## SQLite CLI vs PostgreSQL CLI

| SQLite | PostgreSQL |
|---------|------------|
| `sqlite3` | `psql -U postgres` |
| Opens SQLite CLI | Opens PostgreSQL CLI |
| Opens a local `.db` file | Connects to the PostgreSQL server |
| No server required | Requires a running PostgreSQL server |
| Usually no login required | Requires a PostgreSQL username and password |

---

## Summary

The `psql` program is the official command-line tool for PostgreSQL. It is used to connect to the PostgreSQL server, execute SQL queries, and manage databases using both SQL statements and `psql` meta commands.


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