from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("mysql+pymysql://root:root@localhost:3306/bakeryapp")
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

