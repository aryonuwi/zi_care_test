import datetime

from typing import List
from fastapi import APIRouter,status, HTTPException, Depends
from starlette import  status
from starlette.requests import Request
from starlette.responses import Response
from sqlalchemy.orm import Session
from db_models.models import GroupSequence
from app.sections.schemas import Create,Get,Lists
from app.server import SessionLocal

router = APIRouter()

@router.get("/section")
async def list_section(request:Request):
    with SessionLocal() as session:
        group_sequence = session.query(GroupSequence).all()

    return {"section":group_sequence}

@router.get("/section/{id}", response_model=Get)
async def get_section(request:Request, id:int):
    with SessionLocal() as session:
        group_sequence = session.query(GroupSequence).filter(GroupSequence.id == str(id)).first()
    if group_sequence is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {id} not found")

    return group_sequence.dict()

@router.post("/section", response_model=Get, status_code=status.HTTP_201_CREATED)
async def creat_section(request:Request,  payload: Create):
    with SessionLocal() as session:
        group_sequence = GroupSequence(
            name=payload.name,
        )
        session.add(group_sequence)
        session.commit()
        group_sequence = group_sequence.dict()
    return group_sequence


@router.put("/section/{id}", response_model=Get)
async def update_section(request: Request, id: int, payload: Create):
    with SessionLocal() as session:
        group_sequence = session.query(GroupSequence).filter(
            GroupSequence.id == str(id)).first()
        if group_sequence is None:
            raise HTTPException(status_code=404, detail=f"Poli with ID {id} not found")

        group_sequence.name = payload.name

        session.add(group_sequence)
        session.commit()
        group_sequence = group_sequence.dict()

    return group_sequence

@router.delete("/section/{id}",status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def deleted_section(request: Request, id: int):
    with SessionLocal() as session:
        group_sequence = session.query(GroupSequence).filter(GroupSequence.id == str(id)).first()
        if group_sequence is None:
            raise HTTPException(status_code=404, detail=f"Poli with ID {id} not found")
        session.delete(group_sequence)
        session.commit()