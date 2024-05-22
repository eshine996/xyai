from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from core.pgsql import get_db

SessionDep = Annotated[Session, Depends(get_db)]
