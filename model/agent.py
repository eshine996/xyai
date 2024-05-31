from sqlmodel import Field, SQLModel, Column
from enum import IntEnum
from uuid import UUID
from sqlalchemy_utils import ChoiceType
from model.common import TimeModel


class AgentCategory(IntEnum):
    AgentCategory_BUILDBYOMWER = 1  # 我创建的
    AgentCategory_EfficientWORK = 2  # 效率办公
    AgentCategory_Education = 3  # 教育教学


class AgentBase(SQLModel):
    agent_name: str = Field(title="智能体名称", max_length=16)
    desc: str = Field(title="描述")
    is_public: int = Field(title="是否公共")
    category: AgentCategory = Field(title="智能体类型", sa_column=Column(ChoiceType(AgentCategory)))
    icon: str = Field(title="图标")


class AgentPublic(AgentBase):
    agent_id: UUID = Field(primary_key=True)


class Agent(AgentPublic, TimeModel, table=True):
    tenant_id: UUID
    user_id: UUID
