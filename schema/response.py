from typing import Any, Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class IResponse(BaseModel, Generic[T]):
    code: int
    msg: str
    data: Optional[T] = None


def ok_resp(data: Any = None) -> IResponse:
    resp = IResponse(
        code=200,
        msg="ok",
    )

    if data is not None:
        resp.data = data

    return resp


def fail_resp(msg: str) -> IResponse:
    return IResponse(
        code=400,
        msg=msg
    )
