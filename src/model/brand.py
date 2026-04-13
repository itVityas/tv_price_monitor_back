from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class Brand(BaseModelOnlyId):
    """Модель для бренда товара: id, name, country
    """
    __tablename__ = "brand"
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
