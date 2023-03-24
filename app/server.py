from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:Nuwik3n24k!@localhost:3306/zi_caredb")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)