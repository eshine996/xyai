from sqlmodel import Field, SQLModel, Column
from uuid import UUID
from datetime import datetime
import enum
from sqlalchemy_utils import ChoiceType


class DatasetType(enum.IntEnum):
    DocumentSet = 1  # 文档
    MemoireSet = 2  # 备忘录
    MeetingSet = 3  # 会议记录


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
    tenant_id: UUID
    user_id: UUID
    dataset_id: UUID = Field(primary_key=True)
    dataset_name: str
    desc: str
    dataset_type: DatasetType = Field(sa_column=Column(ChoiceType(DatasetType)))
    created_at: datetime
    deleted_at: datetime | None
