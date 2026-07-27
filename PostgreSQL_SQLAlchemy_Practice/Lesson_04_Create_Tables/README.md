# Lesson 04 - Creating Tables

## Objective

In this lesson, we learn how SQLAlchemy creates database tables from ORM models.

Instead of writing SQL `CREATE TABLE` statements manually, SQLAlchemy reads the model classes and generates the tables automatically.

---

## Topics Covered

- Base.metadata
- create_all()
- Engine
- Creating tables using ORM

---

## What You Learned

- SQLAlchemy can automatically create tables.
- The model class defines the table structure.
- `Base.metadata.create_all()` creates all tables that inherit from Base.

---

## Files

- create_tables.py → Creates PostgreSQL tables from SQLAlchemy models.

---

## Outcome

After completing this lesson, you can create PostgreSQL tables using SQLAlchemy ORM without writing SQL manually.