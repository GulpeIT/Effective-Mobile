from config import settings
from fastapi.routing import APIRouter
from .v1 import router as router_v1

router = APIRouter(prefix=settings.api.prefix)

router.include_router(
    prefix=settings.api.v1.prefix,
    router=router_v1,
)