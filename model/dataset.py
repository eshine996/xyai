from sqlmodel import Field, SQLModel, Column
from uuid import UUID
import enum
from sqlalchemy_utils import ChoiceType
from model.common import TimeModel


class DatasetType(enum.IntEnum):
    DocumentSet = 1  # 文档
    MemoireSet = 2  # 备忘录
    MeetingSet = 3  # 会议记录


class DatasetBase(SQLModel):
    dataset_name: str = Field(title="知识库名称")
    desc: str = Field(title="描述")
    dataset_type: DatasetType = Field(title="类型", sa_column=Column(ChoiceType(DatasetType)))


class Dataset(DatasetBase, TimeModel, table=True):
    tenant_id: UUID
    user_id: UUID
    dataset_id: UUID = Field(primary_key=True)
