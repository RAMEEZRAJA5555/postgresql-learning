# PostgreSQL with Python

## Overview

This folder contains notes and examples for using **PostgreSQL with Python**. It covers connecting Python to PostgreSQL, working with databases using `psycopg2`, understanding SQLAlchemy ORM, performing CRUD operations, managing database sessions, and handling database migrations with Alembic.

These notes are intended for learning modern PostgreSQL development in Python and follow a structured, beginner-friendly approach.

---

## Contents

1. Introduction
2. psycopg2
3. SQLAlchemy ORM
4. Project Structure
5. Database Connection
6. Models
7. CRUD Operations
8. Sessions
9. Alembic
10. Project Architecture

---

## Libraries Used

| Library | Purpose |
|---------|---------|
| psycopg2-binary | Connect Python to PostgreSQL |
| SQLAlchemy | Object Relational Mapping (ORM) |
| Alembic | Database schema migrations |

---

## Learning Objectives

After completing these notes, you will be able to:

- Connect Python with PostgreSQL.
- Execute SQL queries using `psycopg2`.
- Work with SQLAlchemy ORM.
- Create database models.
- Perform CRUD operations.
- Manage database sessions.
- Apply database migrations using Alembic.
- Organize a professional PostgreSQL project.

---

## Project Workflow

```text
Python
   │
   ▼
psycopg2 / SQLAlchemy
   │
   ▼
PostgreSQL Database
   │
   ▼
CRUD Operations
   │
   ▼
Database Migrations (Alembic)
```

---

## Repository Structure

```text
PostgreSQL_with_Python
│
├── 01_Introduction.md
├── 02_psycopg2.md
├── 03_SQLAlchemy_ORM.md
├── 04_Project_Structure.md
├── 05_Database_Connection.md
├── 06_Models.md
├── 07_CRUD_Operations.md
├── 08_Sessions.md
├── 09_Alembic.md
├── 10_Project_Architecture.md
└── README.md
```

---

## Conclusion

This section provides a practical introduction to building PostgreSQL applications with Python. By combining `psycopg2`, SQLAlchemy ORM, and Alembic, developers can create clean, maintainable, and scalable database applications.