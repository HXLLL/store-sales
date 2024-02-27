# api/goods.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.good import GoodCreate, Good, GoodUpdate
from ..crud.crud_good import create_good, get_goods, get_good, update_good, delete_good
from ..models.user import User
from .dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=Good)
def create_good_endpoint(good: GoodCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_good(db=db, good=good, user_id=current_user.id)

@router.get("/", response_model=List[Good])
def read_goods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_goods(db, skip=skip, limit=limit, user_id=current_user.id)

@router.get("/{good_id}", response_model=Good)
def read_good(good_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_good = get_good(db, good_id=good_id)
    if db_good is None or db_good.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Good not found")
    return db_good

@router.patch("/{good_id}", response_model=Good)
def update_good_endpoint(good_id: int, good: GoodUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_good(db=db, good_id=good_id, good=good, user_id=current_user.id)

@router.delete("/{good_id}", response_model=Good)
def delete_good_endpoint(good_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_good(db=db, good_id=good_id, user_id=current_user.id)
