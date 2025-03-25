# init_db.py
from sqlalchemy import create_engine
from models import Base

engine = create_engine("mysql+mysqlconnector://root:root@localhost/punk?charset=utf8mb4")
Base.metadata.create_all(engine)
