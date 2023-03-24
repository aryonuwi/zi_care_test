from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("<database type>://<user>:<password>@<host>:<port>/<database name>")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)