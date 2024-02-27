# schemas/sale_record.py

from pydantic import BaseModel
from datetime import datetime

class SaleRecordBase(BaseModel):
    date: datetime
    quantity_sold: float

class SaleRecordCreate(SaleRecordBase):
    good_id: int

class SaleRecord(SaleRecordBase):
    id: int
    good_id: int

    class Config:
        orm_mode = True
