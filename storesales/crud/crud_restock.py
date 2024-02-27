# crud/crud_restock.py

from sqlalchemy.orm import Session
from ..models.restock_record import RestockRecord
from ..schemas.restock_record import RestockRecordCreate

def create_restock_record(db: Session, restock_record: RestockRecordCreate):
    db_restock_record = RestockRecord(**restock_record.dict())
    db.add(db_restock_record)
    db.commit()
    db.refresh(db_restock_record)
    return db_restock_record

def get_restock_records(db: Session, skip: int = 0, limit: int = 100, good_id: int):
    return db.query(RestockRecord).filter(RestockRecord.good_id == good_id).offset(skip).limit(limit).all()
