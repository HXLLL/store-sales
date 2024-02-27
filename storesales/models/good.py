# models/good.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base_class import Base

class Good(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    quantity = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="goods")
    sales = relationship("SaleRecord", back_populates="good")
    restocks = relationship("RestockRecord", back_populates="good")
