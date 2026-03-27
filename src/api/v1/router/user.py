from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User, db_helper
from core.schemas import UserOut, UserUpdate
from api.v1.dependencies import get_current_active_user


router = APIRouter()


@router.get(
    path="/me",
    response_model=UserOut
)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.put(
    path="/me",
    response_model=UserOut
)
async def update_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(db_helper.session_getter)
):
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)

    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)
    return current_user

@router.delete(
    path="/me",
    status_code=204
)
async def delete_user(
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(db_helper.session_getter)
):
    current_user.is_active = False
    db.add(current_user)
    await db.commit()