from sys import prefix
from fastapi.routing import APIRouter


router = APIRouter()

@router.post(
    prefix="/create"
)
async def create_user():
    pass

@router.delete(
    prefix="/remove"
)
async def delete_user():
    pass