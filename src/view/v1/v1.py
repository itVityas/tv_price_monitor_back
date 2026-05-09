from fastapi import APIRouter

from view.v1.user import router as user_router
from view.v1.currency import router as currency_router
from view.v1.exchange_rate import router as exchange_rate_router
from view.v1.brand import router as brand_router


v1_router = APIRouter()
v1_router.include_router(user_router)
v1_router.include_router(currency_router)
v1_router.include_router(exchange_rate_router)
v1_router.include_router(brand_router)
