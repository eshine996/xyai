# 加密
from datetime import datetime, timedelta
from typing import Any
import jwt
import hashlib

ALGORITHM = "HS256"
SECRET_KEY = "nwnwinv2+_weg][34534080$%^&&"


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Any:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)


def sha256_encrypt(text):
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()
