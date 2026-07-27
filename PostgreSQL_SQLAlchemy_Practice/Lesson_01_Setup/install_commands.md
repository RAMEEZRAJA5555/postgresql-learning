# Installation Commands

## Check Python

```cmd
python --version
```

---

## Check pip

```cmd
pip --version
```

---

## Check PostgreSQL Server

```cmd
pg_isready
```

Expected Output:

```text
:5432 - accepting connections
```

---

## Install SQLAlchemy

```cmd
pip install sqlalchemy
```

---

## Install PostgreSQL Driver

```cmd
pip install psycopg2-binary
```

---

## Verify SQLAlchemy

```cmd
pip show sqlalchemy
```

---

## Verify psycopg2

```cmd
pip show psycopg2-binary
```

---

## Test PostgreSQL

```cmd
psql -U postgres
```

Inside PostgreSQL:

```sql
SELECT version();
```

Exit:

```sql
\q
```