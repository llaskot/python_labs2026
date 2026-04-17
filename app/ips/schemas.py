from typing import Annotated, Optional, Union

from bson import ObjectId
from pydantic import EmailStr, Field, BaseModel, field_validator, ConfigDict, BeforeValidator, IPvAnyAddress, \
    field_serializer


class IpCreate(BaseModel):
    """Save schema"""
    model_config = ConfigDict(
        extra='allow'
    )
    ip: str

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
    ip: IPvAnyAddress


class IpResponse(BaseModel):
    """Save schema"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra='allow'
    )
    id: str = Field(None, alias="_id")
    ip: IPvAnyAddress

    @field_validator("id", mode="before")
    @classmethod
    def transform_id(cls, v: ObjectId) -> str:
        if v is None:
            raise ValueError("ID is missing")
        return str(v)

