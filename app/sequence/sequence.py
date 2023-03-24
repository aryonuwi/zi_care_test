from datetime import date
from datetime import timedelta
from dateutil.parser import parse

from typing import List
from fastapi import APIRouter,status, HTTPException, Depends
from starlette import  status
from starlette.requests import Request
from starlette.responses import Response
from sqlalchemy.orm import Session
from sqlalchemy import text
from db_models.models import Sequence
from app.sequence.schemas import Get,Lists
from app.server import SessionLocal

router = APIRouter()

@router.get("/sequence",response_model=Get)
async def get_latest_call(request:Request):
    with SessionLocal() as session:
        today = date.today()
        yesterday = today - timedelta(days = 1)
        last_yesterday_number = session.query(Sequence)\
            .where(Sequence.call_status=='0')\
            .where(Sequence.created==yesterday)\
            .order_by(Sequence.sequence_number.desc()).first()
        
        if last_yesterday_number is not None:
            last_yesterday_number.call_status = 1
            session.add(last_yesterday_number)
            session.commit()

        if now_sequence() is None:
            sequence_lates =  session.query(Sequence)\
            .where(Sequence.call_status=='1')\
            .order_by(Sequence.sequence_number.desc()).first()
            return sequence_lates.dict()
        

    return now_sequence().dict()

@router.put("/sequence/next", response_model=Get)
async def next_sequence_call(request:Request):
    with SessionLocal() as session:
        lates_sequence = now_sequence()
        
        lates_sequence.call_status = 1
        session.add(lates_sequence)
        session.commit()

        if now_sequence() is None:
            return lates_sequence.dict()

    return now_sequence().dict()

def now_sequence():
    with SessionLocal() as session:
        today = date.today()
        return session.query(Sequence)\
                .where(Sequence.call_status=='0')\
                .where(Sequence.created==today)\
                .first()

@router.post("/sequence", status_code=status.HTTP_201_CREATED)
async def creat_sequence(request:Request):
    with SessionLocal() as session:
        now = date.today()
        # query = text(f'select MAX(sequence_number) as sequence_number  from sequence where group_sequence_id={payload.group_sequence_id} and created="{now}"')
        query = text(f'select MAX(sequence_number) as sequence_number  from sequence where created="{now}"')
        rows = session.execute(query)
        lates_row = ''
        for row in rows:
            lates_row = row

        if lates_row[0] == None:
            sequence_number = 1
        else:
            sequence_number = lates_row[0]+1

        sequence = Sequence(
            created=parse(now.strftime("%Y-%m-%d")),
            sequence_number=sequence_number,
            call_status=0
        )

        session.add(sequence)
        session.commit()
        sequence = sequence.dict()
    return sequence