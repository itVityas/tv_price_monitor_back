from sqlalchemy import Column, String, Boolean

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    def __str__(self):
        return f'<user>: {self.id} {self.username}'
