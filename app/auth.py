from datetime import datetime
from datetime import timedelta
from passlib.context import CryptContext
from jose import jwt
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from .database import SessionLocal
from .models import User

security = HTTPBearer()

SECRET_KEY = "super_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):

    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = (
        datetime.utcnow() +
        timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def get_current_user(
    credentials:
    HTTPAuthorizationCredentials = Depends(
        security
    )
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        db = SessionLocal()

        user = (
            db.query(User)
            .filter(
                User.username == username
            )
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )
        
        db.close()

        return user

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
