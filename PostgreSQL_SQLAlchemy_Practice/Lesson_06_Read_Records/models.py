from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create Base Class
Base = declarative_base()

# Contact Model
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)