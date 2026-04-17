from sqlalchemy.ext.asyncio import AsyncSession

from src.model.category import Category
from .base import BaseData


class CategoryData(BaseData):
    def __init__(self, model: Category, session: AsyncSession):
        super().__init__(
            model=model, session=session
        )
