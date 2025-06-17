from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("mysql+mysqlconnector://root:iYNDMISGpOlvFlewQEhKAVrKjaTIpBNR@shuttle.proxy.rlwy.net:52803/railway")
# mysql+mysqlconnector://root:iYNDMISGpOlvFlewQEhKAVrKjaTIpBNR@shuttle.proxy.rlwy.net:52803/railway
# mysql+pymysql://root:qaws123!@localhost:3306/bakeryapp
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

