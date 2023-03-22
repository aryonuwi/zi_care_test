import datetime

from typing import List
from fastapi import APIRouter,status, HTTPException, Depends
from starlette import  status
from starlette.requests import Request
from starlette.responses import Response
from sqlalchemy.orm import Session
from db_models.models import Sequence
from app.sequence.schemas import Get,Create,Lists
from app.server import SessionLocal

router = APIRouter()

# @router.get("/sequence")
# async def list_patient(request:Request):
#     with SessionLocal() as session:
#         users = session.query(User).all()

#     return {"users":users}

# @router.get("/sequence/{id}", response_model=GetUser)
# async def get_patient(request:Request, id:uuid.UUID):
#     with SessionLocal() as session:
#         user = session.query(User).filter(User.id == str(id)).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail=f"Task with ID {id} not found")
    
#     return user.dict()

# @router.post("/sequence", response_model=GetUser, status_code=status.HTTP_201_CREATED)
# async def creat_patient(request:Request,  payload: UserCreate):
#     with SessionLocal() as session:
#         user = User(
#             created=datetime.datetime.utcnow(),
#             updated=datetime.datetime.utcnow(),
#             name=payload.name,
#             birth_date=payload.birth_date,
#             blood_type=payload.blood_type
#         )
#         session.add(user)
#         session.commit()
#         user = user.dict()
#     return user