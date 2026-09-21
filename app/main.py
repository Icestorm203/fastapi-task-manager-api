from fastapi import FastAPI

from .database import engine
from .database import Base

from .routers.tasks import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)

app.include_router(router)