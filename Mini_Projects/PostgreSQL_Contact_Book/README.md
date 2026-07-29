# PostgreSQL Contact Book

A simple Contact Book application built using **Python**, **PostgreSQL**, and **SQLAlchemy ORM**.

## Features

- Create Contact
- View All Contacts
- Search Contact
- Update Contact
- Delete Contact

## Technologies Used

- Python
- PostgreSQL
- SQLAlchemy
- psycopg2

## Project Structure

```
PostgreSQL_Contact_Book/
│
├── crud.py
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/RAMEEZRAJA5555/postgresql-learning.git
```

Move to the project folder:

```bash
cd PostgreSQL_learning/Mini_Projects/PostgreSQL_Contact_Book
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configure Database

Create a PostgreSQL database.

Update the `DATABASE_URL` in `database.py` with your own:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"
```

## Run the Project

```bash
python main.py
```

## CRUD Operations

- Create Contact
- View All Contacts
- Search Contact
- Update Contact
- Delete Contact

## Author

**Rameez Raja**