# Database Connection Flow

## SQLAlchemy Connection Workflow

```text
Python Program
        │
        ▼
Import SQLAlchemy
        │
        ▼
Create Database URL
        │
        ▼
Create Engine
        │
        ▼
Connect to PostgreSQL
        │
        ▼
Execute SQL Query
        │
        ▼
Receive Results
```

---

## Components

### Database URL

Contains:

- Database type
- Username
- Password
- Host
- Port
- Database name

Example:

```text
postgresql://postgres:password@localhost:5432/sqlalchemy_practice
```

---

### Engine

The Engine is the bridge between Python and PostgreSQL.

It is responsible for:

- Managing database connections
- Sending SQL queries
- Receiving results
- Managing connection pooling

Example:

```python
engine = create_engine(DATABASE_URL)
```

---

### First SQL Query

```python
connection.execute(text("SELECT version();"))
```

This executes a SQL query through SQLAlchemy and returns the PostgreSQL server version.