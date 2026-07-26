# Project Structure

## Introduction

A professional PostgreSQL project should be organized into separate files instead of writing everything in one file. Separating responsibilities makes the project easier to read, maintain, debug, and extend.

---

# Why Project Structure?

Instead of placing all the code inside `main.py`, different files are created for different tasks. This improves code organization and follows professional software development practices.

---

# Typical Project Structure

```text
project/
│
├── database.py
├── models.py
├── crud.py
├── main.py
├── requirements.txt
└── README.md
```

---

# File Responsibilities

### database.py

Contains the database configuration.

- Database URL
- Engine
- Session
- Base

---

### models.py

Contains Python classes that represent database tables.

Example:

```python
class Contact(Base):
    __tablename__ = "contacts"
```

---

### crud.py

Contains all database operations.

Example:

- Create
- Read
- Update
- Delete

---

### main.py

The entry point of the application.

It calls functions from other files and interacts with the user.

---

### requirements.txt

Stores all required Python packages.

Example:

```text
sqlalchemy
psycopg2-binary
alembic
```

---

### README.md

Contains project documentation, installation steps, and project description.

---

# Advantages of Proper Project Structure

- Easy to understand
- Easy to maintain
- Better teamwork
- Reusable code
- Cleaner project organization

---

# Workflow

```text
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

# Conclusion

A well-structured project separates responsibilities into different files. This makes the application more organized, easier to debug, and suitable for real-world software development.