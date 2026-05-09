from datetime import date as datetype
from typing import Optional

from pydantic import BaseModel

from .pagination import PaginationSortParamsSchema
from .currency import CurrencyFullSchema


class ExchangeRateSmallSchema(BaseModel):
    date: datetype
    currency_id: int
    base_currency_id: int
    rate: float

    class Config:
        from_attributes = True


class ExchangeRateFullSchema(BaseModel):
    id: int
    date: datetype
    currency: CurrencyFullSchema
    base_currency: CurrencyFullSchema
    rate: float

    class Config:
        from_attributes = True


class ExchangeRateSimpleSchema(BaseModel):
    id: int
    date: datetype
    currency_id: int
    base_currency_id: int
    rate: float

    class Config:
        from_attributes = True


class ExchangeRatePatchSchema(BaseModel):
    date: Optional[datetype] = None
    rate: Optional[float] = None


class ExchangeRateParamsSchema(PaginationSortParamsSchema):
    id: Optional[int] = None
    date: Optional[datetype] = None
    date_gte: Optional[datetype] = None
    date_lte: Optional[datetype] = None
    currency_id: Optional[int] = None
    base_currency_id: Optional[int] = None
