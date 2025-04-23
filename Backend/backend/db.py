from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("mysql+mysqlconnector://root:iYNDMISGpOlvFlewQEhKAVrKjaTIpBNR@mysql.railway.internal:3306/railway")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

