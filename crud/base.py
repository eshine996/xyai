from typing import TypeVar, Optional
from sqlmodel import SQLModel, Session, select

ModelType = TypeVar("ModelType", bound=SQLModel)


class CRUDBase:
    def __init__(self, model: type[ModelType]):
        self.model = model

    def get_by_id(self, db_session: Session, uid: str) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == uid)
        return db_session.exec(query).one_or_none()

    def delete_by_id(self, db_session: Session, uid: str) -> bool:
        pass
