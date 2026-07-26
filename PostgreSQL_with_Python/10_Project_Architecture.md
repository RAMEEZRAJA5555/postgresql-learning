# Project Architecture

## Introduction

Project Architecture refers to the overall structure of a project and how different files work together. In a SQLAlchemy project, each file has a specific responsibility, making the application clean, organized, and easy to maintain.

---

# Typical Project Architecture

```text
project/
│
├── database.py
├── models.py
├── crud.py
├── main.py
├── requirements.txt
├── alembic/
└── README.md
```

---

# database.py

Responsible for:

- Database URL
- Engine
- Session
- Base

Example:

```python
engine = create_engine(DATABASE_URL)
```

---

# models.py

Contains all database tables as Python classes.

Example:

```python
class Contact(Base):
    __tablename__ = "contacts"
```

---

# crud.py

Contains all database operations.

Examples:

- Create
- Read
- Update
- Delete

Example:

```python
session.add(contact)
session.query(Contact).all()
session.delete(contact)
```

---

# main.py

The starting point of the application.

It imports other files and calls their functions.

Example:

```python
from crud import create_contact

create_contact()
```

---

# requirements.txt

Stores all required Python packages.

Example:

```text
sqlalchemy
psycopg2-binary
alembic
```

Install packages using:

```bash
pip install -r requirements.txt
```

---

# alembic/

Stores migration files used to update the database schema safely.

Common command:

```bash
alembic upgrade head
```

---

# README.md

Contains:

- Project overview
- Installation steps
- Required libraries
- Usage instructions

---

# Complete Architecture Flow

```text
User
   │
   ▼
main.py
   │
   ▼
crud.py
   │
   ▼
models.py
   │
   ▼
database.py
   │
   ▼
PostgreSQL Database
```

---

# Advantages of Good Architecture

- Clean code
- Easy maintenance
- Better teamwork
- Reusable components
- Easier debugging
- Scalable for large projects

---

# Conclusion

A well-designed project architecture separates responsibilities into different files. This improves readability, maintainability, and makes the application suitable for real-world software development using PostgreSQL and SQLAlchemy.