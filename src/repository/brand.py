from sqlalchemy.ext.asyncio import AsyncSession

from src.model.brand import Brand
from src.repository.base import BaseData


class BrandData(BaseData):
    def __init__(self, model: Brand, session: AsyncSession):
        super().__init__(model=model, session=session)