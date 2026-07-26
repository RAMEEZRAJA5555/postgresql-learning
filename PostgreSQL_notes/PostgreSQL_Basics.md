# 1. What is PostgreSQL?

PostgreSQL (Postgres) is a powerful, open-source Relational Database Management System (RDBMS). It is used to store, retrieve, and manage data using SQL. It is widely used because of its reliability, security, and performance.

---

# 2. Features of PostgreSQL

- Open-source and free
- ACID compliant
- Highly secure
- Supports large databases
- Cross-platform
- Extensible and reliable

---

# 3. PostgreSQL Installation

Install PostgreSQL from the official website. During installation, pgAdmin, the PostgreSQL Server, and the psql Command Line Interface (CLI) are installed. After installation, create a password for the `postgres` user.

---

# 4. PostgreSQL Architecture

PostgreSQL consists of:

- Server (stores the databases)
- Database
- Schema
- Tables
- Rows and Columns
- Clients (pgAdmin and psql)

---

# 5. pgAdmin

pgAdmin is PostgreSQL's graphical user interface (GUI). It allows users to create databases, tables, run SQL queries, and manage PostgreSQL without using the command line.

---

# 6. PostgreSQL Command Line (psql)

`psql` is PostgreSQL's Command Line Interface (CLI). It allows users to connect to PostgreSQL, execute SQL queries, and manage databases using commands.

Example:

```bash
psql -U postgres
```

---

# 7. Creating a Database

Create a new database using:

```sql
CREATE DATABASE contact_book;
```

List databases:

```sql
\l
```

Connect to a database:

```sql
\c contact_book
```

---

# 8. Creating Tables

Create a table using the `CREATE TABLE` statement.

```sql
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);
```

...
