from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class ScreenResolution(BaseModelOnlyId):
    name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    width: Mapped[int]
    height: Mapped[int]
