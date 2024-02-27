# models/restock_record.py

from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from .base_class import Base

class RestockRecord(Base):
    __tablename__ = "restock_records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    quantity_restocked = Column(Float)
    good_id = Column(Integer, ForeignKey('goods.id'))

    good = relationship("Good", back_populates="restocks")
