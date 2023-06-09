import uuid

from sqlalchemy import Column,String,DateTime,Integer,ForeignKey,Date,Boolean
from  sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'

    id = Column(String(40), primary_key=True, default=generate_uuid, index=True)
    name = Column(String(225), nullable=False)
    birth_date = Column(DateTime, nullable=False)
    blood_type = Column(String(225), nullable=False)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)

    def dict(self):
        return{
            "id":self.id,
            "name":self.name,
            "birth_date":self.birth_date,
            "blood_type":self.blood_type,
            "created":self.created,
            "updated":self.updated
        }
    
class Sequence(Base):
    __tablename__ = 'sequence'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sequence_number = Column('sequence_number', Integer)
    # group_sequence_id = Column('group_sequence_id', Integer, ForeignKey('group_sequence.id'))
    call_status =  Column(Boolean, nullable=False, default=False)
    created = Column(Date, nullable=False)
    

    def dict(self):
        return{
            "id":self.id,
            "sequence_number":self.sequence_number,
            "created":self.created
        }


# class GroupSequence(Base):
#     __tablename__ = 'group_sequence'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column('name', String(150), nullable=False)
#     def dict(self):
#         return{
#             "id":self.id,
#             "name":self.name
#         }
