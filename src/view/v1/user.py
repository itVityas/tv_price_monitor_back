from fastapi import APIRouter, Depends, HTTPException, status

from schema.user import (
    UserGetSchema,
    UserCreateSchema,
    UserChangePasswordSchema,
    UserChangeActionSchema,
    UserPaginationParamsSchema
)
from repository.user import UserData
from model.user import User
from settings.database import get_session


router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/', response_model=list[UserGetSchema])
async def get_users(
        pagination: UserPaginationParamsSchema = Depends(),
        session=Depends(get_session)):
    """
    Получить список пользователей с пагинацией, сортировкой и фильтрацией

    Параметры пагинации:
    - Страница: ?page=0
    - Количество записей на странице: ?page_size=20

    Параметры сортировки:
    - Сортировка по ID: ?sort_field=id
    - Сортировка по username: ?sort_field=username
    - Сортировка по дате создания: ?sort_field=created_at
    - Сортировка по дате обновления: ?sort_field=updated_at
    - Обратная сортировка: ?sort_field=-id

    Примеры фильтров:
    - Фильтр по username: ?filters[username]=john
    - Фильтр по части username: ?filters[username__icontains]=jo
    - Фильтр по ID: ?filters[id]=1
    - Фильтр по диапазону ID: ?filters[id__gt]=10&filters[id__lt]=50
    - Фильтр по дате: ?filters[created_at__gte]=2024-01-01T00:00:00
    - Несколько фильтров: ?filters[is_active]=true&filters[is_admin]=false
    """
    try:
        user_model = UserData(User, session)
        users = await user_model.get_multi(
            skip=pagination.offset,
            limit=pagination.limit,
            sort_fild=pagination.sort_field,
            sort_order=pagination.sort_order,
            filters=pagination.filters)
        return [UserGetSchema.model_validate(user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post('/', response_model=UserGetSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateSchema, session=Depends(get_session)):
    try:
        user_model = UserData(User, session)
        new_user = await user_model.create(user)
        return UserGetSchema.model_validate(new_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put('/change_password/', response_model=UserGetSchema)
async def change_password_user(user: UserChangePasswordSchema, session=Depends(get_session)):
    try:
        user_data = UserData(User, session)
        model = await user_data.change_password(
            id=user.id, password=user.new_password, old_password=user.old_password)
        return UserGetSchema.model_validate(model)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put('/change_active/', response_model=UserGetSchema)
async def change_active_user(user: UserChangeActionSchema, session=Depends(get_session)):
    try:
        user_data = UserData(User, session)
        model = await user_data.change_state(id=user.id, is_active=user.is_active)
        return UserGetSchema.model_validate(model)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
