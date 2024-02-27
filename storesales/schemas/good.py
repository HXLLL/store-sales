# schemas/good.py

from pydantic import BaseModel

class GoodBase(BaseModel):
    name: str
    category: str

class GoodCreate(GoodBase):
    quantity: float

class GoodUpdate(GoodBase):
    quantity: float

class Good(GoodBase):
    id: int
    user_id: int
    quantity: float

    class Config:
        orm_mode = True
