from typing import Any
import jwt
from pydantic import BaseModel

ALGORITHM = "HS256"
SECRET_KEY = "nwnwinv2+_weg][34534080$%^&&"


class TokenPayload(BaseModel):
    user_id: str
    username: str
    exp: int


def create_access_token(payload: TokenPayload) -> str:
    return jwt.encode(dict(payload), SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Any:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
