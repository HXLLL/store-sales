# api/goods.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from ..crud import crud_good as crud
from ..models.user import User
from ..schemas.good import GoodCreate, Good, GoodUpdate
from ..api.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=Good)
def create_good(
    good: GoodCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new good record for the current user.
    """
    return crud.create_good(db=db, good=good, user_id=current_user.id)

@router.get("/", response_model=List[Good])
def read_goods(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve all goods owned by the current user.
    """
    goods = crud.get_goods(db, user_id=current_user.id, skip=skip, limit=limit)
    return goods

@router.patch("/{good_id}", response_model=Good)
def update_good(
    good_id: int,
    good: GoodUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update a good record.
    """
    db_good = crud.get_good(db, good_id=good_id)
    if not db_good:
        raise HTTPException(status_code=404, detail="Good not found")
    if db_good.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this good")
    
    return crud.update_good(db=db, good_id=good_id, good=good)

@router.delete("/{good_id}", response_model=Good)
def delete_good(
    good_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a good record.
    """
    db_good = crud.get_good(db, good_id=good_id)
    if not db_good:
        raise HTTPException(status_code=404, detail="Good not found")
    if db_good.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this good")
    
    return crud.delete_good(db=db, good_id=good_id)
