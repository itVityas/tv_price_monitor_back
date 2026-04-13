from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class Category(BaseModelOnlyId):
    """Модель для категории товара: id, name
    """
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
