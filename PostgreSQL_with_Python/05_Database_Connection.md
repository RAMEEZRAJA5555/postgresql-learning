# Database Connection

## Introduction

Before performing any database operations, Python must establish a connection with the PostgreSQL database. In SQLAlchemy, the database connection is managed using the **Engine**, **Session**, and **Base** objects.

---

# Database URL

The Database URL contains the information required to connect to PostgreSQL.

Syntax:

```python
DATABASE_URL = "postgresql://username:password@localhost/database_name"
```

Example:

```python
DATABASE_URL = "postgresql://postgres:1234@localhost/contact_book"
```

---

# Creating the Engine

The Engine is responsible for connecting Python with PostgreSQL.

```python
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)
```

---

# Creating SessionLocal

A Session is used to perform database operations.

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
```

Create a session:

```python
session = SessionLocal()
```

---

# Creating Base

The Base class is used to create models (database tables).

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

Every model class will inherit from `Base`.

---

# Complete database.py Example

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1234@localhost/contact_book"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
```

---

# Why Use database.py?

Keeping the database configuration in a separate file makes the project:

- Easy to maintain
- Reusable
- Cleaner
- More organized

Other files simply import `engine`, `SessionLocal`, and `Base` instead of creating new connections.

---

# Workflow

```text
DATABASE_URL
      │
      ▼
create_engine()
      │
      ▼
Engine
      │
      ▼
SessionLocal
      │
      ▼
Database Operations
```

---

# Conclusion

The `database.py` file is the foundation of every SQLAlchemy project. It stores the database configuration and creates the Engine, Session, and Base, which are used throughout the application.