# psycopg2

## Introduction

`psycopg2` is the official PostgreSQL adapter for Python. It allows Python applications to connect directly to a PostgreSQL database and execute SQL queries. It is fast, reliable, and widely used in Python projects.

Unlike SQLAlchemy ORM, `psycopg2` requires developers to write SQL queries manually.

---

# Installing psycopg2

Install the library using pip:

```bash
pip install psycopg2-binary
```

Verify the installation:

```python
import psycopg2
```

If no error appears, the installation was successful.

---

# Connecting to PostgreSQL

Create a database connection:

```python
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="contact_book",
    user="postgres",
    password="your_password"
)
```

---

# Creating a Cursor

A cursor is used to execute SQL queries.

```python
cursor = connection.cursor()
```

---

# Executing SQL Queries

Execute any SQL statement using:

```python
cursor.execute("SELECT * FROM contacts")
```

---

# Fetching Data

Fetch all records:

```python
rows = cursor.fetchall()

for row in rows:
    print(row)
```

Fetch one record:

```python
row = cursor.fetchone()
```

---

# Inserting Data

```python
cursor.execute(
    """
    INSERT INTO contacts(name, phone, email)
    VALUES (%s, %s, %s)
    """,
    ("Ali", "03001234567", "ali@gmail.com")
)

connection.commit()
```

`commit()` saves the changes permanently.

---

# Updating Data

```python
cursor.execute(
    """
    UPDATE contacts
    SET phone=%s
    WHERE contact_id=%s
    """,
    ("03112223333", 1)
)

connection.commit()
```

---

# Deleting Data

```python
cursor.execute(
    """
    DELETE FROM contacts
    WHERE contact_id=%s
    """,
    (1,)
)

connection.commit()
```

---

# Closing the Connection

Always close the cursor and database connection after completing your work.

```python
cursor.close()
connection.close()
```

---

# Advantages of psycopg2

- Official PostgreSQL adapter.
- Fast and lightweight.
- Full control over SQL queries.
- Supports transactions.
- Suitable for small and medium-sized applications.

---

# psycopg2 vs SQLAlchemy

| psycopg2 | SQLAlchemy |
|----------|------------|
| Manual SQL queries | Uses Python objects |
| More SQL knowledge required | Easier to write and maintain |
| Faster for simple tasks | Better for large applications |
| Direct database access | ORM abstraction |

---

# Typical psycopg2 Workflow

```text
Install psycopg2
        │
        ▼
Import psycopg2
        │
        ▼
Create Connection
        │
        ▼
Create Cursor
        │
        ▼
Execute SQL Query
        │
        ▼
Commit Changes
        │
        ▼
Fetch Results
        │
        ▼
Close Cursor
        │
        ▼
Close Connection
```

---

# Conclusion

`psycopg2` is the official PostgreSQL driver for Python. It allows developers to connect Python with PostgreSQL and execute SQL queries directly. It is an excellent choice when full control over SQL is required, while SQLAlchemy is preferred for object-oriented database programming.