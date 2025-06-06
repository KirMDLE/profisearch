from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    family_name: str
    password: str
    secret_code: str


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserLogin(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] | None
    password: Optional[str] | None