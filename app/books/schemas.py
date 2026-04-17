from datetime import datetime
from typing import Optional, Annotated

from bson import ObjectId
from pydantic import BaseModel, AfterValidator, ConfigDict, field_validator
from pydantic import Field

def validate_not_future(v: int) -> int:
    curr = datetime.now().year
    if v > curr:
        raise ValueError(f"Year {v} is in the future (current: {curr})")
    return v
YearType = Annotated[int, Field(ge=1600), AfterValidator(validate_not_future)]
class BookCreate(BaseModel):
    """Registration scheme"""
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    pages: int = Field(..., ge=1)
    year: YearType


class BookUpdate(BaseModel):
    """Update scheme"""
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    pages: Optional[int] = Field(None, ge=1)
    year: YearType | None = None

class BookResponse(BaseModel):
    """response scheme"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
    id: str = Field(None, alias="_id")
    title: str
    author: str
    pages: int
    year: int
    active: bool

    @field_validator("id", mode="before")
    @classmethod
    def transform_id(cls, v: ObjectId) -> str:
        if v is None:
            raise ValueError("ID is missing")
        return str(v)