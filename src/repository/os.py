from sqlalchemy.ext.asyncio import AsyncSession

from src.model.os import OS
from src.repository.base import BaseData

class OSData(BaseData):
    def __init__(self, model: OS, session: AsyncSession):
        super().init(model=model, session=session)