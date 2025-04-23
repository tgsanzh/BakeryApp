from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("mysql+mysqlconnector://root:iYNDMISGpOlvFlewQEhKAVrKjaTIpBNR@shuttle.proxy.rlwy.net:52803/railway")
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

