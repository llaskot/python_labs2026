from datetime import datetime
from typing import Optional

from bson import ObjectId, timestamp
from pydantic import BaseModel, ConfigDict, Field, IPvAnyAddress


class Ip(BaseModel):
    """DB schema"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra='allow'
    )
    id: Optional[ObjectId] = Field(None, alias="_id")
    ip: IPvAnyAddress
    requested_by: list[ObjectId] = Field(default_factory=list)
    requested_at: list[datetime] = Field(default_factory=list)

