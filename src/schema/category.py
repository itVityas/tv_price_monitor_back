from typing import Optional

from pydantic import BaseModel

from .pagination import PaginationSortParamsSchema


class CategorySmallSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryUpdateSchema(BaseModel):
    name: Optional[str] = None

class CategoryFullSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CategoryParamsSchema(PaginationSortParamsSchema):
    id: Optional[int] = None
    name: Optional[str] = None
    name__ne: Optional[str] = None
    name__icontains: Optional[str] = None
    name__istartswith: Optional[str] = None
    name__iendswith: Optional[str] = None
