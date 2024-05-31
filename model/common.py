from sqlmodel import SQLModel, Field
from datetime import datetime


class TimeModel(SQLModel):
    created_at: datetime
    deleted_at: datetime
