from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Backend.backend.db import Base


class Categories(Base):
    __tablename__ = 'Categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(100))

    relationship("Products", back_populates="Categories")