from pydantic import create_model
from typing import Any


def ResponseModel(data: Any = None):
    if data is not None:
        m = create_model('Response', code=(int, ...), msg=(str, ...), data=(data, ...))
    else:
        m = create_model('Response', code=(int, ...), msg=(str, ...))
    return m


def OKResponse(data: Any = None):
    resp = ResponseModel(data)
    resp.code = 200
    resp.msg = "ok"

    if data is not None:
        resp.data = data

    return resp


def FailResponse(msg: str):
    resp = ResponseModel()

    resp.code = 400
    resp.msg = msg
    return resp
