from sqlmodel import SQLModel
from datetime import datetime


class TimeModel(SQLModel):
    created_at: datetime
    deleted_at: datetime | None
