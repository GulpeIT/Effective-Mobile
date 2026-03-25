from config import settings
from fastapi.routing import APIRouter
from .auth import router as router_auth

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(
    prefix=settings.api.v1.auth,
    router=router_auth,
)