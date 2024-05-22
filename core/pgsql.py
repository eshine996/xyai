from sqlmodel import create_engine
from core.config import settings
from sqlmodel import Session
from typing import Generator

engine = create_engine(str(settings.POSTGRES_DATABASE_URI))


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
