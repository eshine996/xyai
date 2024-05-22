from sqlmodel import create_engine
from core.config import settings
from collections.abc import Generator
from sqlmodel import Session

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
