# 数据库
from sqlmodel import create_engine
from config import settings
from sqlmodel import Session
from typing import Generator

db_engine = create_engine(str(settings.POSTGRES_DATABASE_URI))


def get_db() -> Generator[Session, None, None]:
    with Session(db_engine) as session:
        try:
            yield session
        finally:
            session.close()
