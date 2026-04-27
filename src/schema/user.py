from typing import Optional, Dict, Any

from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from schema.pagination import PaginationSortParamsSchema


class UserGetSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    username: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True


class UserFilterSchema(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    username__ne: Optional[str] = None
    username__contains: Optional[str] = None
    username__icontains: Optional[str] = None
    username__startswith: Optional[str] = None
    username__endswith: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
    created_at__gt: Optional[datetime] = None
    created_at__gte: Optional[datetime] = None
    created_at__lt: Optional[datetime] = None
    created_at__lte: Optional[datetime] = None
    updated_at__gt: Optional[datetime] = None
    updated_at__gte: Optional[datetime] = None
    updated_at__lt: Optional[datetime] = None
    updated_at__lte: Optional[datetime] = None

    class Config:
        extra = 'allow'

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.model_dump().items() if v is not None}

    def has_filters(self) -> bool:
        return bool(self.to_dict())


class UserPaginationParamsSchema(PaginationSortParamsSchema):
    filters: Optional[UserFilterSchema] = Field(default=None, description="Фильтры")

    @field_validator('sort_field')
    def validate_sort_field(cls, v):
        allowed_fields = ['id', 'username', 'is_active', 'is_admin', 'created_at', 'updated_at']
        if v not in allowed_fields:
            raise ValueError(f"sort_field must be one of {allowed_fields}")
        return v


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
