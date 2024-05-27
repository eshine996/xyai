from sqlmodel import Field, SQLModel, Column
from uuid import UUID
from enum import IntEnum
from sqlalchemy_utils import ChoiceType
from model.common import TimeModel


class DatasetType(IntEnum):
    DocumentSet = 1  # 文档
    MemoireSet = 2  # 备忘录
    MeetingSet = 3  # 会议记录


class DatasetBackend(IntEnum):
    Backend_XiaoYang = 1
    Backend_Dify = 2


class DatasetBase(SQLModel):
    dataset_name: str = Field(title="知识库名称", max_length=12)
    desc: str = Field(title="描述")
    dataset_type: DatasetType = Field(title="类型", sa_column=Column(ChoiceType(DatasetType)))


class DatasetPublic(DatasetBase):
    dataset_id: UUID = Field(primary_key=True)
    backend: DatasetBackend = Field(title="backend", sa_column=Column(ChoiceType(DatasetBackend)))


class Dataset(DatasetPublic, TimeModel, table=True):
    tenant_id: UUID
    user_id: UUID
