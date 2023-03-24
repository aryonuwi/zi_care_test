from datetime import date
from typing import  List, Optional
from pydantic import BaseModel

class Error(BaseModel):
    detail: Optional[str] = None

# class Create(BaseModel):
#     # group_sequence_id:int


class Get(BaseModel):
    id:int
    sequence_number:int
    created:date

    class  Config:
        orm_mode:True

    
class Lists(BaseModel):
    section_list: List[Get]