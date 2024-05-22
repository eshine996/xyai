from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class IResponse(BaseModel, Generic[T]):
    message: str = ""
    meta: dict | Any | None = {}
    data: T | None = None
