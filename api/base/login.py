from fastapi import APIRouter
from pydantic import BaseModel, Field
from api.deps import SessionDep
from schema.response import IResponse, ok_resp, fail_resp
import crud

router = APIRouter(tags=["登录"])


class LoginReq(BaseModel):
    username: str = Field(..., title="用户名")
    password: str = Field(..., title="密码")


class LoginResp(BaseModel):
    token: str = Field(..., title="token")
    expire: int = Field(..., title="过期时间")


@router.post(path="/api/v1/login", summary="账户密码登录")
def login_by_password(db_session: SessionDep, req: LoginReq) -> IResponse[LoginResp]:
    user = crud.user.get_by_username(username=req.username, db_session=db_session)
    if user is None:
        return fail_resp(msg="密码或账号错误")
    return ok_resp()


class LoginUserInfo(BaseModel):
    username: str
    school_id: str
    school_name: str
    role: str


@router.get(path="/api/v1/login/getUserInfo", summary="获取登录用户信息")
def get_login_user_info(session: SessionDep) -> IResponse[LoginUserInfo]:
    # todo
    pass
