from sqlalchemy.ext.asyncio import AsyncSession

from model.matrix_type import MatrixType
from repository.base import BaseData


class MatrixTypeData(BaseData):
    def __init__(self, model: MatrixType, session: AsyncSession):
        super().__init__(model=model, session=session)
