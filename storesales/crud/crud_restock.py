# crud/crud_restock.py

from sqlalchemy.orm import Session
from typing import List
from ..models.restock_record import RestockRecord
from ..schemas.restock_record import RestockRecordCreate

def create_restock_record(db: Session, restock_record: RestockRecordCreate) -> RestockRecord:
    db_restock_record = RestockRecord(**restock_record.dict())
    db.add(db_restock_record)
    db.commit()
    db.refresh(db_restock_record)
    return db_restock_record

def get_restock_records(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[RestockRecord]:
    return db.query(RestockRecord).filter(RestockRecord.good.has(user_id=user_id)).offset(skip).limit(limit).all()
