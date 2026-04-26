from datetime import datetime

from pydantic import BaseModel

from .pagination import PaginationSortParamsSchema


class UserGetSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    username: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True


user_filters = {
    'id': None,
    'username': None,
    'start_username': None,
    'end_username': None,
    'is_active': None,
    'is_admin': None
}


class UserPaginationParamsSchema(PaginationSortParamsSchema):
    filters: dict = user_filters


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
