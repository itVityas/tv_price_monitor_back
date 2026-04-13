from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class Shop(BaseModelOnlyId):
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    url: Mapped[str] = mapped_column(String(150), nullable=False)
