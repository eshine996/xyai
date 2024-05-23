# 加密
from datetime import datetime, timedelta
from typing import Any
import jwt
from passlib.context import CryptContext

ALGORITHM = "HS256"
SECRET_KEY = "nwnwinv2+_weg][34534080$%^&&"


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Any:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
