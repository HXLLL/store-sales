# schemas/user.py

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    user_id: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str