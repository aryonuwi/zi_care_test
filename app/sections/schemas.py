from datetime import datetime
from typing import  List, Optional
from pydantic import BaseModel

class Error(BaseModel):
    detail: Optional[str] = None

class Create(BaseModel):
    name:str


class Get(BaseModel):
    id:int
    name:str

    class  Config:
        orm_mode:True

    
class Lists(BaseModel):
    section_list: List[Get]