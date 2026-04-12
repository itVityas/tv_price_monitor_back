from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select

from model.user import User
from repository.base import BaseData


class UserData(BaseData):
    def __init__(self, model: User, session: AsyncSession):
        super().__init__(
            model=model, session=session
        )
