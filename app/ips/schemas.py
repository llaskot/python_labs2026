from datetime import datetime, timezone
from typing import Annotated, Optional, Union, Any

from bson import ObjectId
from pydantic import EmailStr, Field, BaseModel, field_validator, ConfigDict, BeforeValidator, IPvAnyAddress, \
    field_serializer


class IpCreate(BaseModel):
    """Save schema"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='allow'
    )
    ip: str
    requested_by: list[ObjectId] = Field(default_factory=list)
    requested_at: list[datetime] = Field(
        default_factory=lambda: [datetime.now(timezone.utc)]
    )

class IpCheck(BaseModel):
    """get schema"""
    ip: IPvAnyAddress
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"ip": "2001:4860:4860::8888"},
                {"ip": "8.8.8.8"}
            ]
        }
    }

class IpUpdate(BaseModel):
    """update schema"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    requested_by: ObjectId
    requested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class IpResponse(BaseModel):
    """Response schema"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra='allow'
    )
    id: str = Field(None, alias="_id")
    ip: IPvAnyAddress
    requested_by: list[str] = Field(exclude=False, default=None)
    requested_at: Any = Field(exclude=False, default=None)

    @field_validator("id", mode="before")
    @classmethod
    def transform_id(cls, v: ObjectId) -> str:
        if v is None:
            raise ValueError("ID is missing")
        return str(v)

    @field_validator("requested_by", mode="before")
    @classmethod
    def transform_requested_by(cls, v: Any) -> list[str]:
        if isinstance(v, list):
            return [str(item) for item in v]
        if v is None:
            return []
        return [str(v)]

