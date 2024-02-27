# models/sale_record.py

from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from .base_class import Base

class SaleRecord(Base):
    __tablename__ = "sale_records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    quantity_sold = Column(Float)
    good_id = Column(Integer, ForeignKey('goods.id'))

    good = relationship("Good", back_populates="sales")
