from config import settings
from fastapi.routing import APIRouter

router = APIRouter(prefix=settings.api.prefix)