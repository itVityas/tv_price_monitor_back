from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now())


class BaseModel(Base, TimestampMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


class BaseModelOnlyId(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
