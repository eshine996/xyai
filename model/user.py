from typing import Optional
from sqlmodel import Field, SQLModel


class user(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
