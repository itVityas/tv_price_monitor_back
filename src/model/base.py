from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False, onupdate=func.now())


class BaseModel(Base, TimestampMixin):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class BaseModelOnlyId(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
