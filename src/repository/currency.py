from sqlalchemy.ext.asyncio import AsyncSession

from src.model.currency import Currency
from src.repository.base import BaseData


class CurrencyData(BaseData):
    def __init__(self, model: Currency, session: AsyncSession):
        super().__init__(model=model, session=session)
