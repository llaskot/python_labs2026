from typing import Annotated, Optional, Union

from pydantic import EmailStr, Field, BaseModel, field_validator, ConfigDict, BeforeValidator


class UserCreate(BaseModel):
    """Creation by admin scheme"""
    email: EmailStr
    login: str = Field(..., min_length=6, max_length=20)
    password: str = Field(..., min_length=6)
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    active: bool = True
    is_admin: bool = False
    is_manager: bool = False

class UserRegistrate(BaseModel):
    """Registration user info scheme"""
    email: EmailStr
    login: str = Field(..., min_length=6, max_length=20)
    password: str = Field(..., min_length=6)
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)



class UserUpdate(BaseModel):
    """Updating by admin scheme"""
    email: EmailStr
    login: Optional[str] = Field(None, min_length=6, max_length=20)
    first_name: Optional[str] = Field(None, min_length=1)
    last_name: Optional[str] = Field(None, min_length=1)
    active: Optional[bool] = Field(None)
    is_admin: Optional[bool] = Field(None)
    is_manager: Optional[bool] = Field(None)


PyObjectId = Annotated[str, BeforeValidator(str)]

class UserResponseAdm(BaseModel):
    """Admin Response schema"""
    id: PyObjectId = Field(alias="_id")
    email: str
    login: str
    first_name: str
    last_name: str
    active: bool
    is_admin: bool
    is_manager: bool

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        protected_namespaces=()
    )

class UserPermissionsDto(BaseModel):
    id: str
    active: bool
    is_admin: bool
    is_manager: bool

    @field_validator("id", mode="before")
    @classmethod
    def serialize_id(cls, v):
        # Если пришел ObjectId, превращаем в строку, иначе оставляем как есть
        return str(v) if v else v

    model_config = {
        "from_attributes": True,
        "populate_by_name": True
    }

class LoginDto(BaseModel):
    login: Union[EmailStr, str] = Field(..., min_length=5, max_length=50)
    password: str = Field(..., min_length=6, max_length=50)