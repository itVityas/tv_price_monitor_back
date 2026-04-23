from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext

from model.user import User
from schema.user import UserCreateSchema
from repository.base import BaseData


class UserData(BaseData):
    def __init__(self, model: User, session: AsyncSession):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        super().__init__(
            model=model, session=session
        )

    def _hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def _verify_password(self, plain_password: str, hash_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hash_password)

    async def get_by_username(self, username: str) -> User:
        query = select(self.model).where(self.model.username == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, obj_in: UserCreateSchema):
        avail_user = await self.get_by_username(obj_in.username)
        if avail_user:
            raise ValueError("Пользователь с таким именем уже существует")
        obj_in.password = self._hash_password(obj_in.password)
        user = User(**obj_in.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user

    async def change_password(self, id: int, new_password: str, old_password: str) -> User:
        query = select(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            raise ValueError("Пользователь не найден")
        if not self._verify_password(old_password, user.password):
            raise ValueError("Неверный пароль")
        if self._verify_password(new_password, user.password):
            raise ValueError("Новый пароль должен отличаться от старого")
        user.password = self._hash_password(new_password)
        self.session.add(user)
        await self.session.commit()
        return user

    async def change_state(self, id: int, is_active: bool) -> User:
        qyery = select(self.model).where(self.model.id == id)
        result = await self.session.execute(qyery)
        user = result.scalar_one_or_none()

        if not user:
            raise ValueError("Пользователь не найден")

        user.is_active = is_active
        self.session.add(user)
        await self.session.commit()
        return user

    async def authenticate(self, username: str, password: str) -> User:
        user = await self.get_by_username(username)
        if not user:
            return None
        if not self._verify_password(password, user.password):
            return None
        return user
