from typing import  Union

from pydantic import EmailStr, Field, BaseModel

from app.users.schemas import UserResponseAdm



class ConfirmationCode(BaseModel):
    conf_code: str = Field(min_length=6, max_length=6)

class LoginResponse(BaseModel):
    user: UserResponseAdm
    access_token: str

