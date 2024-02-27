# api/sale.py

from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from ..crud import crud_sale as crud
from ..schemas.user import User
from ..schemas.sale_record import SaleRecordCreate, SaleRecord
from ..api.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=SaleRecord, status_code=status.HTTP_201_CREATED)
def create_sale_record(
    sale_record: SaleRecordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_sale_record(db=db, sale_record=sale_record)

@router.get("/", response_model=List[SaleRecord])
def read_sale_records(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_sale_records(db=db, user_id=current_user.id, skip=skip, limit=limit)
