from datetime import datetime
from typing import  List, Optional
from pydantic import BaseModel

class Error(BaseModel):
    detail: Optional[str] = None

class Create(BaseModel):
    sequence_number:int
    group_sequence_id:int
    created:datetime


class Get(BaseModel):
    id:int
    sequence_number:int
    group_sequence_id:int
    created:datetime

    class  Config:
        orm_mode:True

    
class Lists(BaseModel):
    section_list: List[Get]