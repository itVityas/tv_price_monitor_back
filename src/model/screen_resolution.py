from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModelOnlyId


class ScreenResolution(BaseModelOnlyId):
    """Модель для предоставления разрешения экрана телевизора: id, name, width, height
    """
    __tablename__ = 'screen_resolution'
    name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    width: Mapped[int]
    height: Mapped[int]

    def __str__(self):
        return f'<name>: {self.id} {self.name}'
