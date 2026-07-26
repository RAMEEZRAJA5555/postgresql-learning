# PostgreSQL with Python

## Introduction

PostgreSQL is a powerful Relational Database Management System (RDBMS) used to store and manage data. While PostgreSQL can be accessed directly using SQL commands through **pgAdmin** or the **psql Command Line Interface (CLI)**, Python provides an easier and more efficient way to interact with databases.

Python allows developers to connect to PostgreSQL, execute SQL queries, retrieve data, and build complete database applications. Instead of manually writing SQL for every operation, Python libraries make database programming simpler and more organized.

There are two common ways to work with PostgreSQL in Python:

### 1. psycopg2

`psycopg2` is the official PostgreSQL adapter for Python. It allows Python programs to connect directly to a PostgreSQL database and execute SQL queries manually.

Example:

```python
import psycopg2
```

With `psycopg2`, developers write SQL statements such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE` inside Python code.

---

### 2. SQLAlchemy ORM

SQLAlchemy is a Python library that provides an **Object Relational Mapping (ORM)** system. Instead of writing SQL queries manually, developers work with Python classes and objects.

Example:

```python
user = User(name="Ali")

session.add(user)
session.commit()
```

SQLAlchemy automatically converts Python code into SQL queries, making applications cleaner, easier to maintain, and more suitable for large projects.

---

## PostgreSQL with Python Workflow

```text
Install PostgreSQL
        │
        ▼
Install Python Libraries
        │
        ▼
Connect to PostgreSQL
        │
        ▼
Execute SQL Queries
        │
        ▼
Retrieve or Modify Data
        │
        ▼
Build Complete Applications
```

---

## Libraries Used

| Library | Purpose |
|---------|---------|
| psycopg2 | Connect Python to PostgreSQL using SQL queries |
| SQLAlchemy | ORM library for working with database objects |
| Alembic | Database migration tool for SQLAlchemy |

---

## What You Will Learn

In this section, you will learn:

- Connecting Python with PostgreSQL.
- Using the `psycopg2` library.
- Understanding SQLAlchemy ORM.
- Creating models and database sessions.
- Performing CRUD operations.
- Managing database migrations using Alembic.
- Organizing a professional PostgreSQL project.

---

## Conclusion

PostgreSQL with Python combines the power of PostgreSQL with Python's simplicity. Developers can either use **psycopg2** for direct SQL execution or **SQLAlchemy ORM** for object-oriented database programming. Both approaches are widely used in modern software development.