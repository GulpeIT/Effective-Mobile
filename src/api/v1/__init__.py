from config import settings
from fastapi.routing import APIRouter
from .router.auth import router as router_auth
from .router.user import router as router_user

router = APIRouter()

router.include_router(
    tags=["🔐 auth"],
    prefix=settings.api.v1.auth,
    router=router_auth,
)

router.include_router(
    tags=["👤 user"],
    prefix=settings.api.v1.user,
    router=router_user,
)