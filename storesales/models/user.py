# models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    goods = relationship("Good", back_populates="owner")
