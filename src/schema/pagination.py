from typing import List, TypeVar, Generic

from pydantic import BaseModel, Field


T = TypeVar('T')


class PaginationParamsSchema(BaseModel):
    page: int = Field(default=1, ge=1, description='Номер страницы, начинается с 1')
    page_size: int = Field(default=20, ge=1, le=100, description='Размер страницы, с 1 до 100')

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        return self.page_size


class PaginationSortParamsSchema(BaseModel):
    page: int = Field(default=1, ge=1, description='Номер страницы, начинается с 1')
    page_size: int = Field(default=20, ge=1, le=100, description='Размер страницы, с 1 до 100')
    sort_field: str = Field(default='id', description='Поле для сортировки')
    sort_order: str = Field(default='asc', description='Порядок сортировки: asc или desc')

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        return self.page_size


class PaginationResponseSchema(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int

    @classmethod
    def create(cls, items: List[T], total: int, page: int, size: int) -> "PaginationResponseSchema[T]":
        pages = (total + size - 1) // size if size > 0 else 0
        return cls(
            items=items,
            total=total,
            page=page,
            size=size,
            pages=pages
        )


class PaginationSortResponseSchema(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int
    sort_field: str
    sort_order: str

    @classmethod
    def create(cls, items: List[T], total: int,
               page: int, size: int, sort_field: str, sort_order: str) -> "PaginationSortResponseSchema[T]":
        pages = (total + size - 1) // size if size > 0 else 0
        return cls(
            items=items,
            total=total,
            page=page,
            size=size,
            pages=pages,
            sort_field=sort_field,
            sort_order=sort_order
        )
