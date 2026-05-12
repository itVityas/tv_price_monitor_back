from fastapi import APIRouter

from view.v1.user import router as user_router
from view.v1.currency import router as currency_router
from view.v1.exchange_rate import router as exchange_rate_router
from view.v1.brand import router as brand_router
from view.v1.category import router as category_router
from view.v1.matrix_type import router as matrix_type_router
from view.v1.os import router as os_router
from view.v1.shop import router as shop_router
from view.v1.screen_resolution import router as screen_resolution_router


v1_router = APIRouter()
v1_router.include_router(user_router)
v1_router.include_router(currency_router)
v1_router.include_router(exchange_rate_router)
v1_router.include_router(brand_router)
v1_router.include_router(category_router)
v1_router.include_router(matrix_type_router)
v1_router.include_router(os_router)
v1_router.include_router(shop_router)
v1_router.include_router(screen_resolution_router)
