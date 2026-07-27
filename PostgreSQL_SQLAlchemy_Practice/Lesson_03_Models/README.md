# Lesson 03 - SQLAlchemy Models

## Objective

In this lesson, we learn how SQLAlchemy ORM represents a database table as a Python class.

Instead of writing SQL CREATE TABLE statements manually, we define a model class. SQLAlchemy uses this model to create the corresponding table in PostgreSQL.

---

## Topics Covered

- ORM Model
- Base Class
- Table Name
- Columns
- Data Types
- Primary Key

---

## What You Learned

- Every table is represented by a Python class.
- Every column is represented by a Python attribute.
- SQLAlchemy converts Python classes into PostgreSQL tables.
- Models make database operations easier without writing SQL manually.

---

## Files

- models.py → Defines the Contact model using SQLAlchemy ORM.

---

## Outcome

After completing this lesson, you can create ORM models that represent database tables.