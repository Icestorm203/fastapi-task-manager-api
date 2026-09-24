from fastapi import APIRouter
from fastapi import HTTPException

from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate
from ..schemas import UserLogin

from ..auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    tags=["Auth"]
)

@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(
            User.username == user.username
        )
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        username=user.username,
        password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()

    return {
        "message": "User registered"
    }


@router.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    db_user = (
        db.query(User)
        .filter(
            User.username == user.username
        )
        .first()
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

