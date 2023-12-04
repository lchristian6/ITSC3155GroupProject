from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pizza_name = Column(String(100))
    price = Column(Integer)

    #order_details = relationship("OrderDetail", back_populates="order")
    #customers = relationship("Customer", back_populates="orders")