from datetime import datetime
from typing import  List, Optional
from uuid import UUID
from pydantic import BaseModel
 
class Error(BaseModel):
    detail: Optional[str] = None
    
class UserCreate(BaseModel):
    name: str
    birth_date: datetime
    blood_type: str
    created: datetime
    updated: datetime
 
class GetUser(BaseModel):
    id: UUID
    name: str
    birth_date: datetime
    blood_type: str
    created: datetime
    updated: datetime

 
    class Config:
        orm_mode = True


class ListUserSchema(BaseModel):
    users: List[GetUser]