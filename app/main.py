from fastapi import FastAPI

from .database import engine
from .database import Base

from .routers.tasks import router
from .routers.auth import router as auth_router

app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():

    Base.metadata.create_all(bind=engine)


app.include_router(router)
app.include_router(auth_router)