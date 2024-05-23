from crud.base_crud import CRUDBase
from model import User
from sqlmodel import select
from sqlmodel import Session
from typing import Optional


class CRUDUser(CRUDBase[User]):

    def get_by_username(self, username: str, db_session: Optional[Session] = None) -> Optional[User]:
        db_session = db_session or super().get_db_session()
        query = select(User).where(User.username == username)
        return db_session.execute(query).scalar_one_or_none()


user = CRUDUser(User)
