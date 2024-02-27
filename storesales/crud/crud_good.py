# crud/crud_good.py

from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.good import Good
from ..schemas.good import GoodCreate, GoodUpdate

def create_good(db: Session, good: GoodCreate, user_id: int) -> Good:
    db_good = Good(**good.dict(), user_id=user_id)
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good

def get_goods(db: Session, skip: int = 0, limit: int = 100, user_id: Optional[int] = None) -> List[Good]:
    if user_id is not None:
        return db.query(Good).filter(Good.user_id == user_id).offset(skip).limit(limit).all()
    return db.query(Good).offset(skip).limit(limit).all()

def get_good(db: Session, good_id: int) -> Optional[Good]:
    return db.query(Good).filter(Good.id == good_id).first()

def update_good(db: Session, good_id: int, good: GoodUpdate) -> Good:
    db_good = db.query(Good).filter(Good.id == good_id).first()
    if db_good:
        update_data = good.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_good, key, value)
        db.commit()
        db.refresh(db_good)
    return db_good

def delete_good(db: Session, good_id: int) -> Good:
    db_good = db.query(Good).filter(Good.id == good_id).first()
    if db_good:
        db.delete(db_good)
        db.commit()
    return db_good
