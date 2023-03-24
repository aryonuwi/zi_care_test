import datetime
import uuid

from typing import List
from fastapi import APIRouter,status, HTTPException, Depends
from starlette import  status
from starlette.requests import Request
from starlette.responses import Response
from sqlalchemy.orm import Session
from db_models.models import User
from app.patients.schemas import UserCreate,GetUser,ListUserSchema
from app.server import SessionLocal

router = APIRouter()

@router.get("/patient")
async def list_patient(request:Request):
    with SessionLocal() as session:
        users = session.query(User).all()

    return {"users":users}

@router.get("/patient/{id}", response_model=GetUser)
async def get_patient(request:Request, id:uuid.UUID):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == str(id)).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {id} not found")
    
    return user.dict()

@router.post("/patient", response_model=GetUser, status_code=status.HTTP_201_CREATED)
async def creat_patient(request:Request,  payload: UserCreate):
    with SessionLocal() as session:
        user = User(
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            name=payload.name,
            birth_date=payload.birth_date,
            blood_type=payload.blood_type
        )
        session.add(user)
        session.commit()
        user = user.dict()
    return user


@router.put("/patient/{id}", response_model=GetUser)
async def update_patient(request: Request, id: uuid.UUID, payload: UserCreate):
    with SessionLocal() as session:
        user = session.query(User).filter(
            User.id == str(id)).first()
        if user is None:
            raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
        
        user.name = payload.name
        user.birth_date = payload.birth_date
        user.blood_type = payload.blood_type
        user.updated = datetime.datetime.utcnow()
        session.add(user)
        session.commit()
        user = user.dict()
    
    return user

@router.delete("/patient/{id}",status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def deleted_patient(request: Request, id: uuid.UUID):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == str(id)).first()
        if user is None:
            raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
        session.delete(user)
        session.commit()