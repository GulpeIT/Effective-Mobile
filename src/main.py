import uvicorn
from api import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.models import db_helper
from config import settings
from app_log import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("app start")
    
    yield
    await db_helper.dispose()
    logger.info("app close")

app = FastAPI(
    debug=True,
    lifespan=lifespan,
)

origins = ["http://localhost:8000", "http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host=settings.run.host, 
        port=settings.run.port, 
        reload=True
        )