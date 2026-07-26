# PostgreSQL with SQLAlchemy ORM

## Introduction

When working with PostgreSQL in Python, we usually do **not** write SQL queries manually for every database operation. Instead, we use **SQLAlchemy**, which is a powerful **Object Relational Mapping (ORM)** library.

SQLAlchemy allows developers to work with **Python classes, objects, and methods** instead of writing SQL queries like `INSERT`, `SELECT`, `UPDATE`, and `DELETE` manually. It automatically converts Python code into SQL queries and sends them to the PostgreSQL database.

This approach makes the code cleaner, easier to read, easier to maintain, and more suitable for large professional applications.

---

# Contents

1. Production Database
2. Why Raw SQL Becomes a Maintenance Problem
3. ORM (Object Relational Mapping)
4. Raw SQL vs ORM
5. Project Structure
6. Installing SQLAlchemy & psycopg2-binary
7. database.py
8. Engine
9. models.py
10. Creating Tables
11. CRUD Operations
12. Read Records
13. Read One Record
14. Update Records
15. Delete Records
16. Session
17. Python with SQLAlchemy
18. Alembic
19. Alembic Revision
20. Real Project Architecture

---

# 1. Production Database

A production database is the live database used by real users. It stores actual application data and must be secure, reliable, and easy to maintain.

---

# 2. Why Raw SQL Becomes a Maintenance Problem

Writing SQL queries manually is called **Raw SQL**. It is suitable for small projects, but in large projects hundreds of SQL queries become difficult to manage. If the database structure changes, many SQL queries must also be modified.

---

# 3. ORM (Object Relational Mapping)

ORM is a technique that maps Python classes and objects to database tables and records. Instead of writing SQL manually, developers write Python code, and SQLAlchemy automatically generates the SQL queries.

---

# 4. Raw SQL vs ORM

### Raw SQL

- SQL queries are written manually.
- Best for small projects.
- Harder to maintain.

### ORM

- Uses Python classes and objects.
- SQL is generated automatically.
- Cleaner and easier to maintain.

---

# 5. Project Structure

A professional SQLAlchemy project is divided into separate files.

```text
project/
│
├── database.py
├── models.py
├── crud.py
├── main.py
└── requirements.txt
```

Each file has a specific responsibility, making the project easier to understand and maintain.

---

# 6. Installing SQLAlchemy & psycopg2-binary

Install SQLAlchemy:

```bash
pip install sqlalchemy
```

Install PostgreSQL Driver:

```bash
pip install psycopg2-binary
```

- **SQLAlchemy** → ORM Library
- **psycopg2-binary** → PostgreSQL Driver

---

# 7. database.py

The `database.py` file contains the database configuration.

It usually defines:

- Database URL
- Engine
- Session
- Base

Other files import these objects instead of creating new database connections.

---

# 8. Engine

An **Engine** is the connection manager between Python and PostgreSQL.

```python
engine = create_engine(DATABASE_URL)
```

It manages database connections and is later used to create Sessions.

---

# 9. models.py

The `models.py` file defines database tables using Python classes.

- One class = One table
- One class attribute = One table column

Example:

```python
class Contact(Base):
```

---

# 10. Creating Tables

SQLAlchemy creates tables automatically using:

```python
Base.metadata.create_all(engine)
```

This creates all tables defined inside the model classes.

---

# 11. CRUD Operations

CRUD stands for:

- Create
- Read
- Update
- Delete

These are the four basic database operations performed using SQLAlchemy Sessions.

---

# 12. Read Records

Retrieve all records using:

```python
session.query(Contact).all()
```

`.all()` returns every record as Python objects.

---

# 13. Read One Record

Retrieve a specific record using:

```python
session.query(Contact).filter_by(contact_id=1).first()
```

- `filter_by()` applies a condition.
- `first()` returns the first matching object.

---

# 14. Update Records

Updating follows three simple steps:

1. Retrieve the object.
2. Modify its attributes.
3. Save changes using:

```python
session.commit()
```

---

# 15. Delete Records

Deleting also follows three steps:

1. Retrieve the object.
2. Delete it using:

```python
session.delete(contact)
```

3. Save changes using:

```python
session.commit()
```

---

# 16. Session

A **Session** is the main object used to communicate with the database.

Common methods:

- `session.add()`
- `session.query()`
- `session.delete()`
- `session.commit()`
- `session.close()`

SQLite uses **Connection + Cursor**, while SQLAlchemy uses **Session**.

---

# 17. Python with SQLAlchemy

Typical SQLAlchemy workflow:

```text
Create Session
      ↓
Perform CRUD
      ↓
Commit Changes
      ↓
Close Session
```

---

# 18. Alembic

Alembic is SQLAlchemy's migration tool.

It updates the database structure without deleting existing data.

It is used when adding, removing, or modifying tables and columns.

---

# 19. Alembic Revision

Create a migration:

```bash
alembic revision --autogenerate -m "Add address column"
```

Apply the migration:

```bash
alembic upgrade head
```

This safely updates the database schema.

---

# 20. Real Project Architecture

A professional SQLAlchemy project usually follows this structure:

```text
project/
│
├── database.py
├── models.py
├── crud.py
├── main.py
├── requirements.txt
└── alembic/
```

Separating responsibilities into different files makes the project cleaner, easier to maintain, and suitable for teamwork.




# SQLAlchemy Quick Code Reference

## 1. Import Required Modules

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
```

---

## 2. Database Connection (database.py)

```python
DATABASE_URL = "postgresql://username:password@localhost/database_name"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
```

---

## 3. Create a Model (models.py)

```python
class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
```

---

## 4. Create Tables

```python
Base.metadata.create_all(engine)
```

---

## 5. Create a Session

```python
session = SessionLocal()
```

---

## 6. Create (Insert)

```python
contact = Contact(
    name="Ali",
    phone="03001234567",
    email="ali@gmail.com"
)

session.add(contact)
session.commit()
```

---

## 7. Read All Records

```python
contacts = session.query(Contact).all()
```

---

## 8. Read One Record

```python
contact = session.query(Contact).filter_by(contact_id=1).first()
```

---

## 9. Update Record

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

contact.phone = "03112223333"

session.commit()
```

---

## 10. Delete Record

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

session.delete(contact)

session.commit()
```

---

## 11. Close Session

```python
session.close()
```

---

## 12. Install Required Packages

```bash
pip install sqlalchemy

pip install psycopg2-binary

pip install alembic
```

---

## 13. Alembic Migration

Create migration:

```bash
alembic revision --autogenerate -m "Create contacts table"
```

Apply migration:

```bash
alembic upgrade head
```

---

## 14. Typical SQLAlchemy Workflow

```text
Install Packages
       ↓
database.py
       ↓
models.py
       ↓
Base.metadata.create_all()
       ↓
SessionLocal()
       ↓
CRUD Operations
       ↓
session.commit()
       ↓
session.close()
```