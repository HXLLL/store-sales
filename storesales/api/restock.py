# api/restock.py

from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from ..crud import crud_restock as crud
from ..schemas.user import User
from ..schemas.restock_record import RestockRecordCreate, RestockRecord
from ..api.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=RestockRecord, status_code=status.HTTP_201_CREATED)
def create_restock_record(
    restock_record: RestockRecordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_restock_record(db=db, restock_record=restock_record)

@router.get("/", response_model=List[RestockRecord])
def read_restock_records(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_restock_records(db=db, user_id=current_user.id, skip=skip, limit=limit)
