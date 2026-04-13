from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class MatrixType(BaseModelOnlyId):
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
