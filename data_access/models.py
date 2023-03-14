import uuid

from sqlalchemy import Column,String,DateTime
from  sqlalchemy.orm import declarative_base, relationship

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


