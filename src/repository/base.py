from typing import TypeVar, Type, Optional, List, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# from pydantic import BaseModel


ModelType = TypeVar("ModelType")
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseData:
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, obj_in: Type[ModelType]):
        db_obj = self.model(**obj_in.model_dump())
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def get_one(self, id: int):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def update(self, id: int, obj_in: Type[ModelType]) -> ModelType:
        db_obj = await self.get(id)
        for field, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, field, value)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def get_multi(
                            self,
                            skip: int = 0,
                            limit: int = 100,
                            filters: Optional[Dict[str, Any]] = None,
                            sort: Optional[str] = None,
                            sort_order: str = "asc"
                        ) -> List[ModelType]:
        """Return model and total count

        Args:
            skip (int, optional): Defaults to 0.
            limit (int, optional): Defaults to 100.
            filters (Optional[Dict[str, Any]], optional): Defaults to None.

        Returns:
            List[ModelType], int : return list of models and total count
        """
        query = select(self.model).offset(skip).limit(limit)
        if filters:
            for filter in filters:
                if hasattr(self.model, filter):
                    query = query.where(
                        getattr(self.model, filter) == filters[filter])
        result = await self.session.execute(query)
        return result.scalars().all()
