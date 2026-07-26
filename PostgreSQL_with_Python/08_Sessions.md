# Sessions

## Introduction

A **Session** is one of the most important components in SQLAlchemy. It acts as a bridge between the Python application and the PostgreSQL database. All database operations such as Create, Read, Update, and Delete (CRUD) are performed through a Session.

---

# Creating a Session

First, create a Session object using `SessionLocal`.

```python
from database import SessionLocal

session = SessionLocal()
```

---

# Adding Data

Use the Session to add objects to the database.

```python
new_contact = Contact(
    name="Ali",
    phone="03001234567",
    email="ali@gmail.com"
)

session.add(new_contact)
session.commit()
```

---

# Reading Data

Retrieve records using the Session.

```python
contacts = session.query(Contact).all()
```

Retrieve one record.

```python
contact = session.query(Contact).filter_by(contact_id=1).first()
```

---

# Updating Data

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

contact.phone = "03112223344"

session.commit()
```

---

# Deleting Data

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

session.delete(contact)

session.commit()
```

---

# Committing Changes

After making changes, save them permanently.

```python
session.commit()
```

---

# Rolling Back Changes

If an error occurs, cancel all uncommitted changes.

```python
session.rollback()
```

---

# Closing the Session

Always close the Session after completing database operations.

```python
session.close()
```

---

# Why Sessions are Important

- Manage database transactions.
- Execute CRUD operations.
- Commit or rollback changes.
- Improve application performance.
- Keep database communication organized.

---

# Session Workflow

```text
Create Session
      │
      ▼
Perform CRUD Operations
      │
      ▼
Commit / Rollback
      │
      ▼
Close Session
```

---

# Conclusion

A Session is the primary interface between Python and PostgreSQL in SQLAlchemy. It manages transactions, performs database operations, and ensures data consistency throughout the application.