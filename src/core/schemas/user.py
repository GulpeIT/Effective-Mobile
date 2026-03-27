from typing import Optional
from pydantic import Field, field_validator
from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict
)

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    surname: str
    patronymic: str
    password: str = Field(..., min_length=6)
    confirm_password: str
    
    
    @field_validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return 


class UserUpdate(BaseModel):
    name: Optional[str] = None
    patronymic: Optional[str] = None
    surname: Optional[str] = None


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: Optional[str] = None
    patronymic: Optional[str] = None
    surname: Optional[str] = None
    is_active: bool