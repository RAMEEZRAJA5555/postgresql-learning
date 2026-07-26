# SQLAlchemy ORM

## Introduction

SQLAlchemy is a powerful Python library that provides **Object Relational Mapping (ORM)** for relational databases such as PostgreSQL. Instead of writing SQL queries manually, developers work with Python classes and objects, and SQLAlchemy automatically generates SQL queries.

---

# Why Use SQLAlchemy?

- Reduces manual SQL writing.
- Cleaner and more readable code.
- Easy to maintain large projects.
- Supports multiple database systems.
- Integrates well with Python applications.

---

# ORM (Object Relational Mapping)

ORM is a technique that maps Python classes to database tables and Python objects to database records.

Example:

```python
class Contact(Base):
    __tablename__ = "contacts"
```

Instead of writing:

```sql
INSERT INTO contacts ...
```

You simply write:

```python
contact = Contact(name="Ali")
```

---

# Installing SQLAlchemy

Install SQLAlchemy using:

```bash
pip install sqlalchemy
```

For PostgreSQL, install the driver:

```bash
pip install psycopg2-binary
```

---

# SQLAlchemy Components

A SQLAlchemy application mainly consists of:

- Engine
- Session
- Base
- Models
- CRUD Operations

---

# Creating the Engine

The engine manages the connection between Python and PostgreSQL.

```python
engine = create_engine(DATABASE_URL)
```

---

# Creating a Session

A Session is used to communicate with the database.

```python
SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()
```

---

# Creating Models

Each Python class represents a database table.

```python
class Contact(Base):
    __tablename__ = "contacts"
```

---

# Creating Tables

SQLAlchemy automatically creates tables.

```python
Base.metadata.create_all(engine)
```

---

# CRUD Operations

The four basic database operations are:

- Create
- Read
- Update
- Delete

Examples:

```python
session.add(contact)
```

```python
session.query(Contact).all()
```

```python
session.commit()
```

```python
session.delete(contact)
```

---

# SQLAlchemy Workflow

```text
Install SQLAlchemy
        │
        ▼
Create Engine
        │
        ▼
Create Session
        │
        ▼
Create Models
        │
        ▼
Create Tables
        │
        ▼
Perform CRUD Operations
        │
        ▼
Commit Changes
        │
        ▼
Close Session
```

---

# Advantages of SQLAlchemy

- Object-oriented programming.
- Less SQL code.
- Easy maintenance.
- Database independent.
- Suitable for professional applications.

---

# Conclusion

SQLAlchemy ORM simplifies database programming by allowing developers to work with Python classes instead of writing SQL queries manually. It is one of the most popular ORM libraries used with PostgreSQL in modern Python applications.