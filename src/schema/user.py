from datetime import datetime

from pydantic import BaseModel


class UserGetSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    username: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    username: str
    is_admin: bool
    password: str

    class Config:
        from_attributes = True


class UserChangePasswordSchema(BaseModel):
    id: int
    old_password: str
    new_password: str

    class Config:
        from_attributes = True


class UserChangeActionSchema(BaseModel):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
