from sqlalchemy.ext.asyncio import AsyncSession

from model.os import OS
from repository.base import BaseData


class OSData(BaseData):
    def __init__(self, model: OS, session: AsyncSession):
        super().__init__(model=model, session=session)
