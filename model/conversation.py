from sqlmodel import Field, SQLModel
from uuid import UUID
from model.common import TimeModel


class ConversationBase(SQLModel):
    title: str


class ConversationPublic(ConversationBase):
    conversation_id: UUID = Field(primary_key=True)
    agent_id: UUID


class Conversation(ConversationPublic, TimeModel, table=True):
    tenant_id: UUID
    user_id: UUID
