# we wrote these 2 lines,to import creae_engine and sessionmaker,which are available in sqlalchemy library,we will use in each database.py file

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL Database URL
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/sqlalchemy_practice"

# Create Engine
engine = create_engine(DATABASE_URL)

# Create Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

print("Database connection configured successfully!")