from sqlalchemy.ext.asyncio import AsyncSession

from model.screen_resolution import ScreenResolution
from repository.base import BaseData


class ScreenResolutionData(BaseData):
    def __init__(self, model: ScreenResolution, session: AsyncSession):
        super().__init__(
            model=model, session=session
        )
