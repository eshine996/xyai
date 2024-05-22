from fastapi import APIRouter
from pydantic import BaseModel, Field
from api.deps import SessionDep
from api.common import ResponseModel

router = APIRouter(tags=["登录"])


class LoginReq(BaseModel):
    username: str = Field(..., title="用户名")
    password: str = Field(..., title="密码")


@router.post(path="/api/v1/login", summary="账户密码登录")
def login_by_password(session: SessionDep, req: LoginReq) -> ResponseModel():
    # todo
    pass


class LoginUserInfo(BaseModel):
    username: str
    school_id: str
    school_name: str
    role: str


@router.get(path="/api/v1/login/getUserInfo", summary="获取登录用户信息")
def get_login_user_info(session: SessionDep) -> ResponseModel(data=LoginUserInfo):
    # todo
    pass
