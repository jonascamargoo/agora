from typing import Optional
from datetime import datetime, timezone # Importe timezone
from uuid import UUID
from sqlmodel import Field, SQLModel

class Group(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="group.id")
    nickname: str
    text: str
    timestamp_client: Optional[datetime] = None
    timestamp_server: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    idempotency_key: UUID = Field(unique=True, index=True)