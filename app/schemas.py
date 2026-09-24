from pydantic import BaseModel
from pydantic import ConfigDict

class TaskCreate(BaseModel):
    title: str


class TaskResponse(BaseModel):
    id: int
    title: str
    is_closed: bool

    model_config = ConfigDict(
        from_attributes=True
    )


class UserCreate(BaseModel):

    username: str

    password: str


class UserLogin(BaseModel):

    username: str

    password: str