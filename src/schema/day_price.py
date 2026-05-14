from typing import Optional
from datetime import date as idate

from pydantic import BaseModel

from .currency import CurrencyFullSchema
from .shop_link import ShopLinkResponceFullSchema
from .pagination import PaginationSortParamsSchema


class DayPriceUpdateSchema(BaseModel):
    shop_link_id: Optional[int] = None
    currency_id: Optional[int] = None
    price: Optional[float] = None
    discount_price: Optional[float] = None
    card_price: Optional[float] = None
    date: Optional[idate] = None

    class Config:
        from_attributes = True


class DayPricePostSchema(BaseModel):
    shop_link_id: int
    currency_id: int
    price: float
    discount_price: Optional[float] = None
    card_price: Optional[float] = None
    date: idate

    class Config:
        from_attributes = True


class DayPriceSmallResponseSchema(BaseModel):
    id: int
    shop_link_id: int
    currency_id: int
    price: float
    discount_price: float
    card_price: float
    date: idate

    class Config:
        from_attributes = True


class DayPriceFullResponseSchema(BaseModel):
    id: int
    shop_link: ShopLinkResponceFullSchema
    currency: CurrencyFullSchema
    price: float
    discount_price: float
    card_price: float
    date: idate

    class Config:
        from_attributes = True


class DayPriceFilterSchema(PaginationSortParamsSchema):
    id: Optional[int] = None
    shop_link_id: Optional[int] = None
    currency_id: Optional[int] = None
    price: Optional[float] = None
    discount_price: Optional[float] = None
    card_price: Optional[float] = None
    date: Optional[str] = None
    date__gte: Optional[str] = None
    date__lte: Optional[str] = None
