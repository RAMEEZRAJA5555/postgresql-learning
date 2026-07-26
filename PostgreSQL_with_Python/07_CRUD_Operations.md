# CRUD Operations

## Introduction

CRUD stands for **Create, Read, Update, and Delete**. These are the four basic operations performed on a database. In SQLAlchemy, CRUD operations are performed using a **Session** object instead of writing SQL queries manually.

---

# Create (Insert)

Create a new object and save it to the database.

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

# Read (Select)

Retrieve all records from the database.

```python
contacts = session.query(Contact).all()

for contact in contacts:
    print(contact.name)
```

Retrieve a single record.

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

print(contact.name)
```

---

# Update

Retrieve the object, modify its attributes, and commit the changes.

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

contact.phone = "03112223344"

session.commit()
```

---

# Delete

Retrieve the object and remove it from the database.

```python
contact = session.query(Contact).filter_by(contact_id=1).first()

session.delete(contact)

session.commit()
```

---

# Commit Changes

Changes are not permanently saved until:

```python
session.commit()
```

---

# Rollback

If an error occurs, undo the changes.

```python
session.rollback()
```

---

# Closing the Session

Always close the session after completing database operations.

```python
session.close()
```

---

# CRUD Workflow

```text
Create Session
      │
      ▼
Create / Read / Update / Delete
      │
      ▼
Commit Changes
      │
      ▼
Close Session
```

---

# Advantages of SQLAlchemy CRUD

- Less code.
- Object-oriented programming.
- Cleaner than raw SQL.
- Easy to maintain.
- Suitable for large projects.

---

# Conclusion

CRUD operations are the core of every database application. SQLAlchemy provides a simple and object-oriented way to create, read, update, and delete records without writing SQL queries manually.