from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Backend.backend.db import Base


class CartItems(Base):
    __tablename__ = 'CartItems'
    cart_item_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    product_id = Column(Integer, ForeignKey('Products.product_id'))
    quantity = Column(Integer, default=1)

    relationship("Users", back_populates="CartItems")
    Products = relationship("Products", back_populates="CartItems")