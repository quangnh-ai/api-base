from pydantic import BaseModel, EmailStr
import typing

class UserBase(BaseModel):
    user_name: str = None
    email: EmailStr = None
    is_active: bool = True

class UserOut(UserBase):
    pass

class UserCreate(UserBase):
    password: str

    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    password: typing.Optional[str] = None

    class Config:
        from_attributes = True

class User(UserBase):
    id: int

    class Config:
        from_attributes = True