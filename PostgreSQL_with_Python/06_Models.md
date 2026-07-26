# Models

## Introduction

In SQLAlchemy, a **Model** is a Python class that represents a table in the database. Each class attribute represents a column, and each object represents a row in the table.

Instead of creating tables manually using SQL, SQLAlchemy allows us to define tables using Python classes.

---

# Creating a Model

Every model inherits from the `Base` class.

```python
from sqlalchemy import Column, Integer, String
from database import Base

class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
```

---

# __tablename__

The `__tablename__` variable specifies the name of the table in PostgreSQL.

Example:

```python
__tablename__ = "contacts"
```

This creates a table named **contacts**.

---

# Columns

Each attribute in the model becomes a column in the database.

Example:

```python
name = Column(String)
phone = Column(String)
email = Column(String)
```

---

# Primary Key

A primary key uniquely identifies each record.

Example:

```python
contact_id = Column(Integer, primary_key=True)
```

---

# Common Data Types

| SQLAlchemy | PostgreSQL |
|------------|------------|
| Integer | INTEGER |
| String | VARCHAR |
| Boolean | BOOLEAN |
| Float | FLOAT |
| Date | DATE |
| DateTime | TIMESTAMP |

---

# Creating Tables

After defining models, create all tables using:

```python
Base.metadata.create_all(engine)
```

---

# Example Model

```python
from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
```

---

# Benefits of Models

- No need to write CREATE TABLE queries.
- Easy to modify tables.
- Cleaner and more readable code.
- Object-oriented database design.

---

# Workflow

```text
Create Base
      │
      ▼
Create Model Class
      │
      ▼
Define Columns
      │
      ▼
Create Tables
      │
      ▼
Store Data
```

---

# Conclusion

Models are the foundation of SQLAlchemy ORM. They define the structure of database tables using Python classes, making database programming simple, clean, and object-oriented.