# PostgreSQL Installation and Setup

## Download PostgreSQL

Download PostgreSQL from the official website:

https://www.postgresql.org/download/

For Windows, the installer is provided by **EnterpriseDB (EDB)**.

---

## Components Installed

Installing PostgreSQL also installs:

- PostgreSQL Server
- pgAdmin 4 (GUI)
- psql (Command-Line Interface)
- PostgreSQL Command Line Tools

---

## Check PostgreSQL Server

After installation, open **Command Prompt (CMD)** and run:

```bash
pg_isready
```

If the output is:

```text
localhost:5432 - accepting connections
```

it means:

- PostgreSQL is installed.
- The PostgreSQL server is running.
- The server is ready to accept connections.

---

## PostgreSQL Server vs SQLite

| SQLite | PostgreSQL |
|---------|------------|
| No database server | Requires a PostgreSQL server |
| Opens a local `.db` file | Connects to a running server |
| No server status check | Use `pg_isready` to check the server |

---

## Summary

Before working with PostgreSQL, make sure the server is running. The `pg_isready` command verifies that the PostgreSQL server is active and ready for connections.