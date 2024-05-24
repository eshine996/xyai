from typing import Annotated
from fastapi import Depends, Header, HTTPException
from utils.storage import Storage
from sqlmodel import Session
from extension.db import get_db
from extension.storage import get_storage
from model import User
from api.token import decode_access_token


def get_current_user(xy_ai_token: str = Header(None)) -> User:
    if not xy_ai_token:
        raise HTTPException(status_code=401, detail="unauthorized")

    try:
        payload = decode_access_token(xy_ai_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

    user = User(
        user_id=payload.get("user_id"),
        username=payload.get("username")
    )
    return user


def get_tenant_id(tenant_id: str = Header(...)) -> str:
    return tenant_id


SessionDep = Annotated[Session, Depends(get_db)]
StorageDep = Annotated[Storage, Depends(get_storage)]
TenantIdDep = Annotated[str, Depends(get_tenant_id)]
CurrentUserDep = Annotated[User, Depends(get_current_user)]
