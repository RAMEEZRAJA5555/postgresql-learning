# PostgreSQL Command-Line Interface (CLI)

## What is psql?

`psql` is the official Command-Line Interface (CLI) for PostgreSQL. It allows users to connect to a PostgreSQL server and execute SQL commands.

Before connecting, check whether the PostgreSQL server is running:

```bash
pg_isready
```

If the output is:

```text
localhost:5432 - accepting connections
```

then the PostgreSQL server is running and ready to accept connections.

---

## Connect to PostgreSQL

Connect as the default superuser:

```bash
psql -U postgres
```

Connect to a specific database:

```bash
psql -U postgres -d mydb -h localhost -p 5432
```

### Command Options

| Option | Description |
|---------|-------------|
| `psql` | Starts the PostgreSQL CLI |
| `-U` | Specifies the username |
| `postgres` | Default PostgreSQL superuser |
| `-d mydb` | Connects to the `mydb` database |
| `-h localhost` | Connects to the local PostgreSQL server |
| `-p 5432` | Uses the default PostgreSQL port |

---

## Common psql Commands

| Command | Description |
|---------|-------------|
| `\l` | List all databases |
| `\c mydb` | Connect to the `mydb` database |
| `\dt` | List all tables in the current database |
| `\d users` | Describe the `users` table |
| `\du` | List all users (roles) |
| `\q` | Quit psql |
| `\?` | Show help for psql commands |
| `\h SELECT` | Show help for the SQL `SELECT` command |

---

## psql Commands vs SQL Commands

**psql Commands (Meta Commands)**

These commands begin with a backslash (`\`) and are executed by the `psql` program.

Examples:

```text
\l
\c
\dt
\d
\du
\q
```

**SQL Commands**

These are standard SQL statements executed by the PostgreSQL server.

Examples:

```sql
CREATE DATABASE bookstore;

CREATE TABLE books (...);

INSERT INTO books VALUES (...);

SELECT * FROM books;
```

---

## SQLite CLI vs PostgreSQL CLI

| SQLite | PostgreSQL |
|---------|------------|
| `sqlite3` | `psql -U postgres` |
| Opens SQLite CLI | Opens PostgreSQL CLI |
| Opens a local `.db` file | Connects to the PostgreSQL server |
| No server required | Requires a running PostgreSQL server |
| Usually no login required | Requires a PostgreSQL username and password |

---

## Summary

The `psql` program is the official command-line tool for PostgreSQL. It is used to connect to the PostgreSQL server, execute SQL queries, and manage databases using both SQL statements and `psql` meta commands.