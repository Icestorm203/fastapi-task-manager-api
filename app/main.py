from fastapi import FastAPI

from .routers.tasks import router
from .routers.auth import router as auth_router

app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)


app.include_router(router)
app.include_router(auth_router)