from sqlmodel import Field, SQLModel
from enum import Enum
from uuid import UUID
from datetime import datetime


class DatasetType(Enum):
    DocumentSet = 1
    MemoireSet = 2
    MeetingSet = 3


class Tenant(SQLModel, table=True):
    tenant_id: UUID = Field(primary_key=True)
    tenant_name: str
    created_at: datetime
    deleted_at: datetime | None


class User(SQLModel, table=True):
    tenant_id: str
    user_id: str = Field(primary_key=True)
    username: str
    password: str


class Dataset(SQLModel, table=True):
    tenant_id: str
    user_id: str
    dataset_id: str = Field(primary_key=True)
    dataset_name: str
    desc: str
    dataset_type: DatasetType
    created_at: int
    deleted_at: int
