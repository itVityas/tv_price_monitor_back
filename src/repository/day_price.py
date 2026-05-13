from sqlalchemy.ext.asyncio import AsyncSession

from model.day_price import DayPrice
from repository.base import BaseData


class DayPriceData(BaseData):
    def __init__(self, model: DayPrice, session: AsyncSession):
        super().__init__(model=model, session=session)
