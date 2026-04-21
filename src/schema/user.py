from datetime import datetime

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str
    password: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True


class UserGetSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
