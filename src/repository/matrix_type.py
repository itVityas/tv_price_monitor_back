from sqlalchemy.ext.asyncio import AsyncSession

from src.model.matrix_type import MatrixType
from src.repository.base import BaseData


class MatrixTypeData(BaseData):
    def __init__(self, model: MatrixType, session: AsyncSession):
        super().__init__(model=model, session=session)
