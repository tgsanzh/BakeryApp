from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from Backend.backend.db import Base


class Products(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    image_url = Column(Text)
    is_active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('Categories.category_id'))

    relationship("Categories", back_populates="Products")
    relationship("OrderItems", back_populates="Products")
    CartItems = relationship("CartItems", back_populates="Products")