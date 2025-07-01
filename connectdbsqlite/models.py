from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from connectdbsqlite.db import Base

class User(Base):
    __tablename__ = "users" #table name in the db
    id = Column(Integer, primary_key=True, index=True) # primary key, index=True - create an index for the column
    name = Column(String, index=True) 
    age = Column(Integer)
    email = Column(String, unique=True, index=True) # unique=True - no duplicate values in the column
    password = Column(String)
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")