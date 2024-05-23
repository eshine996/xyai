from typing import TypeVar, Optional, Generic
from sqlmodel import SQLModel, Session, select
from fastapi import Depends
from extension.db import get_db

ModelType = TypeVar("ModelType", bound=SQLModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    @staticmethod
    def get_db_session() -> Session:
        return next(get_db())

    def get_by_id(self, db_session: Session, uid: str) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == uid)
        return db_session.exec(query).one_or_none()

    def delete_by_id(self, db_session: Session, uid: str) -> bool:
        pass
