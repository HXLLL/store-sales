# crud/crud_sale.py

from sqlalchemy.orm import Session
from typing import List
from ..models.sale_record import SaleRecord
from ..schemas.sale_record import SaleRecordCreate

def create_sale_record(db: Session, sale_record: SaleRecordCreate) -> SaleRecord:
    db_sale_record = SaleRecord(**sale_record.dict())
    db.add(db_sale_record)
    db.commit()
    db.refresh(db_sale_record)
    return db_sale_record

def get_sale_records(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[SaleRecord]:
    return db.query(SaleRecord).filter(SaleRecord.good.has(user_id=user_id)).offset(skip).limit(limit).all()
