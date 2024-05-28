from typing import List, Union, Optional
from datetime import date

from pydantic import BaseModel

class ItemBase(BaseModel):
    title:str
    description: Optional[str] = None
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id:int
        
class UserBase(BaseModel):
    email: Union[str, None] = None
    
class UserCreate(UserBase):
    username: str
    password: str
    full_name: Union[str, None] = None
    
class User(UserBase):
    id: int
    full_name: Union[str, None] = None
    username: str
    is_active: Union[bool, None] = None
    items: List[Item] = []
    
    class Config:
        orm_mode = True