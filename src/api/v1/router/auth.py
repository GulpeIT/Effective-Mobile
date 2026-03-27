from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import db_helper
from core.models import User
from core.schemas import (
    UserCreate,
    UserOut,
    Token
)
from api.v1.encoder import (
    get_password_hash,
    verify_password,
    create_access_token
)


router = APIRouter()


@router.post(
    path="/register",
    response_model=UserOut,
)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(db_helper.session_getter)
    ):
    result = await db.execute(select(User).where(User.email == user_data.email))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = get_password_hash(user_data.password)
    
    db_user = User(
        email=user_data.email,
        first_name=user_data.name,
        last_name=user_data.patronymic,
        middle_name=user_data.surname,
        hashed_password=hashed_password,
        is_active=True
    )
    
    db.add(db_user)
    
    await db.commit()
    await db.refresh(db_user)
    
    return db_user


@router.post(
    path="/login",
    response_model=Token,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(db_helper.session_getter)
):
    result = await db.execute(select(User).where(User.email == form_data.username))
    user: User = result.scalar_one_or_none()

    if not user or not verify_password(form_data.password, user.name):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account is deactivated"
        )

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
async def logout():
    return {"message": "Successfully logged out"}