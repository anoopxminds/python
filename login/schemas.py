from typing import Union
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    password: str
    
    
class User(UserBase):
    id: int
    first_name: Union[str, None] = None
    last_name:  Union[str, None] = None
    created_at: datetime
    updated_at: datetime
    
class UserCreate(UserBase):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    created_at: datetime
    updated_at: datetime