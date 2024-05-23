from fastapi import APIRouter
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.response import IResponse, ok_resp, fail_resp
import crud
from extension.security import sha256_encrypt
from api.token import TokenPayload, create_access_token
from datetime import datetime
from config import settings

router = APIRouter(tags=["登录"])


class LoginReq(BaseModel):
    username: str = Field(..., title="用户名")
    password: str = Field(..., title="密码")


class LoginResp(BaseModel):
    token: str = Field(..., title="token")
    expire: int = Field(..., title="过期时间")


@router.post(path="/login", summary="账户密码登录")
def login_by_password(db_session: SessionDep, req: LoginReq) -> IResponse[LoginResp]:
    user = crud.user.get_by_username(username=req.username, db_session=db_session)
    if not user:
        return fail_resp(msg="密码或账号错误")

    if user.password != sha256_encrypt(req.password):
        return fail_resp(msg="密码或账号错误")

    payload = TokenPayload(
        user_id=str(user.user_id),
        username=user.username,
        exp=int(datetime.utcnow().timestamp()) + settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    resp_data = LoginResp(token=create_access_token(payload), expire=payload.exp)
    return ok_resp(data=resp_data)


class LoginUserInfo(BaseModel):
    username: str
    school_id: str
    school_name: str
    role: str


@router.get(path="/api/v1/login/getUserInfo", summary="获取登录用户信息")
def get_login_user_info(session: SessionDep) -> IResponse[LoginUserInfo]:
    # todo
    pass
