# app/models.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    is_verified: bool = False

    class Config:
        orm_mode = True

# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserInDB(BaseModel):
    email: str
    username: str
    is_verified: bool
    password: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
