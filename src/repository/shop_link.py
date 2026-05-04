from sqlalchemy.ext.asyncio import AsyncSession

from src.model.shop_link import ShopLink
from src.repository.base import BaseData


class ShopLinkData(BaseData):
    def __init__(self, model: ShopLink, session: AsyncSession):
        super().__init__(model=model, session=session)
