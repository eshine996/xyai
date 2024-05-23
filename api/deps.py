from typing import Annotated
from fastapi import Depends
from utils.storage import Storage
from sqlmodel import Session
from core.db import get_db
from core.storage import get_storage

SessionDep = Annotated[Session, Depends(get_db)]
StorageDep = Annotated[Storage, Depends(get_storage)]
