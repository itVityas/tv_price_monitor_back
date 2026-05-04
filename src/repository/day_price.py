from sqlalchemy.ext.asyncio import AsyncSession

from src.model.day_price import DayPrice
from src.repository.base import BaseData


class DayPriceData(BaseData):
    def __init__(self, model: DayPrice, session: AsyncSession):
        super().__init__(model=model, session=session)
