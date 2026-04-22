from fastapi import APIRouter, Depends, HTTPException, status

from schema.user import UserGetSchema, UserCreateSchema, UserChangePasswordSchema
from repository.user import UserData
from model.user import User
from settings.database import get_session


router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/', response_model=list[UserGetSchema])
async def get_users(session=Depends(get_session)):
    try:
        user_model = UserData(User, session)
        users = await user_model.get_multi()
        return [UserGetSchema.model_validate(user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post('/', response_model=UserGetSchema | None)
async def create_user(user: UserCreateSchema, session=Depends(get_session)):
    try:
        user_model = UserData(User, session)
        new_user = await user_model.create(user)
        return UserGetSchema.model_validate(new_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put('/change_password/', tags=["Users"])
async def change_password_user(user: UserChangePasswordSchema, session=Depends(get_session)):
    try:
        user_model = UserData(User, session)
        await user_model.change_password(user)
        return {'status': 'success'}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
