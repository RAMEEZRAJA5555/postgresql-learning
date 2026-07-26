# Alembic

## Introduction

Alembic is the official database migration tool for SQLAlchemy. It helps developers manage changes to the database schema without manually modifying tables or losing existing data.

---

# Why Use Alembic?

As projects grow, database tables often need changes such as:

- Adding new columns
- Removing columns
- Renaming tables
- Modifying data types

Instead of recreating the database, Alembic applies these changes safely using migrations.

---

# Installing Alembic

Install Alembic using pip:

```bash
pip install alembic
```

---

# Initialize Alembic

Create the Alembic project files.

```bash
alembic init alembic
```

This creates:

```text
alembic/
│
├── versions/
├── env.py
├── script.py.mako
└── alembic.ini
```

---

# Configure Database URL

Open **alembic.ini** and update the database URL.

```text
sqlalchemy.url = postgresql://postgres:1234@localhost/contact_book
```

---

# Create Migration

Generate a migration file automatically.

```bash
alembic revision --autogenerate -m "Create contacts table"
```

A new migration file will be created inside the **versions** folder.

---

# Apply Migration

Apply all pending migrations.

```bash
alembic upgrade head
```

---

# Downgrade Migration

Rollback the latest migration.

```bash
alembic downgrade -1
```

Rollback all migrations.

```bash
alembic downgrade base
```

---

# Migration Workflow

```text
Modify Models
      │
      ▼
Generate Migration
      │
      ▼
Review Migration
      │
      ▼
Upgrade Database
```

---

# Advantages of Alembic

- Safe database updates.
- Version control for database schema.
- Works directly with SQLAlchemy.
- Easy rollback of changes.
- Suitable for production projects.

---

# Conclusion

Alembic is an essential tool for SQLAlchemy projects. It allows developers to manage database schema changes safely through versioned migrations without deleting existing data.