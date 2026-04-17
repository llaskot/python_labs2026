from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic import Field
from bson import ObjectId


class Book(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
    id: Optional[ObjectId] = Field(None, alias="_id")
    title: str
    author: str
    year: int
    pages: int
    active: bool = True
