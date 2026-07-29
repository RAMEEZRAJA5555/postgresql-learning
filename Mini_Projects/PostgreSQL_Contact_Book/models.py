from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Contact(Base):
    __tablename__="contacts"

    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)