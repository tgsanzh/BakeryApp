from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from Backend.backend.db import Base


class OrderItems(Base):
    __tablename__ = 'OrderItems'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('Orders.order_id'))
    product_id = Column(Integer, ForeignKey('Products.product_id'))
    quantity = Column(Integer)
    price = Column(DECIMAL(10, 2))

    relationship("Orders", back_populates="OrderItems")
    relationship("Products", back_populates="OrderItems")