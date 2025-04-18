from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from Backend.backend.db import Base


class Orders(Base):
    __tablename__ = 'Orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    total_amount = Column(DECIMAL(10, 2))
    status = Column(String(50))
    delivery_address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    relationship("Users", back_populates="Orders")
    relationship("OrderItems", back_populates="Orders")
