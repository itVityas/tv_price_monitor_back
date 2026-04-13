from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class OS(BaseModelOnlyId):
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
