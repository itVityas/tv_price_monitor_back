from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class MatrixType(BaseModelOnlyId):
    """Модель для предоставления типа матрицы телевизора: id, name
    """
    __tablename__ = "matrix_type"
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
