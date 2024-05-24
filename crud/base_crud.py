from typing import TypeVar, Generic
from sqlmodel import SQLModel, Session
from extension.db import get_db

ModelType = TypeVar("ModelType", bound=SQLModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    @staticmethod
    def get_db_session() -> Session:
        return next(get_db())
