# schemas/restock_record.py

from pydantic import BaseModel
from datetime import datetime

class RestockRecordBase(BaseModel):
    date: datetime
    quantity_restocked: float

class RestockRecordCreate(RestockRecordBase):
    good_id: int

class RestockRecord(RestockRecordBase):
    id: int
    good_id: int

    class Config:
        orm_mode = True
