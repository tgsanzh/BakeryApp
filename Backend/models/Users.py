from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Backend.backend.db import Base


class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(20), unique=True, index=True)
    password = Column(String(500))

    relationship("Orders", back_populates="Users")
    relationship("CartItems", back_populates="Users")