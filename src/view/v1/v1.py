from fastapi import APIRouter

from view.v1.user import router as user_router
from view.v1.currency import router as currency_router


v1_router = APIRouter()
v1_router.include_router(user_router)
v1_router.include_router(currency_router)
