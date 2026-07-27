# PostgreSQL CRUD Operations

## Introduction

CRUD stands for **Create, Read, Update, and Delete**. These are the four basic operations used to manage data in a PostgreSQL table.

---

# Contents

1. What is CRUD?
2. INSERT (Create)
3. SELECT (Read)
4. UPDATE
5. DELETE
6. WHERE Clause
7. Practice Example
8. Summary

---

# 1. What is CRUD?

CRUD represents the four basic database operations:

- Create → Insert new records
- Read → Retrieve records
- Update → Modify existing records
- Delete → Remove records

---

# 2. INSERT (Create)

Insert a new record into a table.

```sql
INSERT INTO contacts(name, phone, email)
VALUES
('Ali', '03001234567', 'ali@gmail.com');
```

Insert multiple records:

```sql
INSERT INTO contacts(name, phone, email)
VALUES
('Ahmed', '03111234567', 'ahmed@gmail.com'),
('Sara', '03221234567', 'sara@gmail.com');
```

---

# 3. SELECT (Read)

Display all records:

```sql
SELECT * FROM contacts;
```

Display selected columns:

```sql
SELECT name, phone
FROM contacts;
```

Retrieve a specific record:

```sql
SELECT *
FROM contacts
WHERE contact_id = 1;
```

---

# 4. UPDATE

Modify existing data.

```sql
UPDATE contacts
SET phone = '03331234567'
WHERE contact_id = 1;
```

Update multiple columns:

```sql
UPDATE contacts
SET
name = 'Ali Khan',
email = 'alikhan@gmail.com'
WHERE contact_id = 1;
```

---

# 5. DELETE

Delete a specific record.

```sql
DELETE FROM contacts
WHERE contact_id = 1;
```

Delete all records:

```sql
DELETE FROM contacts;
```

---

# 6. WHERE Clause

The `WHERE` clause specifies which records should be affected.

Example:

```sql
SELECT *
FROM contacts
WHERE name = 'Sara';
```

Without `WHERE`, all rows are affected.

---

# 7. Practice Example

Create a table:

```sql
CREATE TABLE contacts(
    contact_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);
```

Insert data:

```sql
INSERT INTO contacts(name, phone, email)
VALUES
('Ali', '03001234567', 'ali@gmail.com');
```

Read:

```sql
SELECT * FROM contacts;
```

Update:

```sql
UPDATE contacts
SET phone='03110000000'
WHERE contact_id=1;
```

Delete:

```sql
DELETE FROM contacts
WHERE contact_id=1;
```

---

# 8. Summary

In this lesson, we learned:

- INSERT → Add records
- SELECT → Read records
- UPDATE → Modify records
- DELETE → Remove records
- WHERE → Filter records

CRUD operations are the most commonly used SQL commands for managing data in PostgreSQL.